import sys
from time import process_time_ns

from DataStructures.AST_muFHML import AST
from DataStructures.Configuration import Configuration
from DataStructures.Environment import Environment
from DataStructures.FRA import FRA
from DataStructures.Formulas import Formula
from DataStructures.ParityGames import FRAParity
from DataStructures.Parser import parse_formula
from oink.OinkRunner import parity_game_solver, did_defender_win
from xml_to_FRA import parse_xml


with open("./logic_parser/Logic.g4", "r", encoding='utf-8') as f:
    lines = list(f.readlines())
    lines = lines[3:]
    logic_grammar = ''.join(lines)

instructions = """
**************************<Tool Name>**************************

To run the tool, please use the following command:
python run.py <FRA_File> <formula_file>

Where:
\t - <FRA_File> is the path to the input fresh-register automaton (given as an XML file)
\t - <formula_file> is the path to the Fresh muHML formula, given as per the grammar below

For the (fresh)-register automaton file, the XML file should have as root a <register-automaton> element, with the following child elements:
 - <states>
 - <initial-state>
 - <transitions>
 - <final-state>
 
In the <states> element, you can declare many states, where each state is of the form:
<state>
    <id>{state_name}</id>
    <available-registers>
        <register>{i}</register>
        <register>{j}</register>
        ...
    </available-registers>
</state>

If a state has no available registers, then the state can be of the form:
<state>
    <id>{state_name}</id>
    <available-registers/>
</state>

The initial state is simply of the form:
<initial-state>{state_name}</initial-state>

And similarly for each final-state:
<final-state>{state_name}</final-state>

As for <transitions>, this will contain one child element for each transition of the form:
<transition>
    <from>{source state}</from>
    <input>{transition tag}</input>
    <op>{LFresh, GFresh, or Read}</op>
    <register>{i}</register>
    <to>{target state}</to>
</transition> 

Note that the input element for each transition is optional. 

As for the muHML formula, this can be stored in a text file that adheres to the following grammar:

"""
instructions += logic_grammar

if len(sys.argv) < 3:
    print(instructions)
else:
    fra_file, mhml_file= sys.argv[1], sys.argv[2]

    solver = None
    if len(sys.argv) == 4:
        solver = sys.argv[3]

    fra_parsed = parse_xml(fra_file)
    with open(mhml_file, "r", encoding='utf-8') as f:
        text = ''.join(f.readlines())
        formula_parsed = parse_formula(text)
    time = process_time_ns()
    fra = FRA(*fra_parsed)
    formula_ast = AST(formula_parsed)
    env = Environment()
    formula = Formula.fromAST(formula_ast, env)
    config = Configuration(0, len(fra.registers))
    game = FRAParity.build(fra, config, formula, env.alternationDepths())
    oink_input = game.parity_game_lines()
    output = parity_game_solver(oink_input, "./oink_bin/")
    time = (process_time_ns() - time) / (10 ** 9)
    print("Defender won:", did_defender_win(output['stdout']))
    print("Time Taken:", time, "seconds")
