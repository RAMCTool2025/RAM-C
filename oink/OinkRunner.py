import subprocess
import platform

from DataStructures.AST_muFHML import AST
from DataStructures.Configuration import Configuration
from DataStructures.FRA import FRA
from DataStructures.Formulas import Formula
from DataStructures.Environment import Environment
from DataStructures.ParityGames import FRAParity
from DataStructures.Parser import parse_formula


def parity_game_solver(pg_text: str, oink_path="./oink_bin/", solver="zlk"):
    is_windows = platform.system() == "Windows"

    if is_windows:
        cmd = [
            "wsl",
            "bash",
            "-c",
            f"{oink_path}oink -v -p"
        ]
    else:
        cmd = [
            f"{oink_path}oink", "-v", "-p"
        ]
    result = subprocess.run(
        cmd,
        input = pg_text,
        capture_output = True,
        text=True,
        encoding="utf-8"
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "exit_code": result.returncode
    }

# If the game was given with labels, then include it as input
# to find if the initial node wins. Otherwise, check if node
# in line 0 wins.
def did_defender_win(output: str, G=None) -> bool:
    nd0 = None if G==None else str(G.S[0]).replace(" ","")
    for line in output.splitlines():
        if line.__contains__("won by even:"):
            parts = line.split(":")[1].strip().split()
            for part in parts:
                if nd0 == None:
                    node_id, winner = map(int, part.split("/"))
                    if node_id == 0: return True
                else:
                    if part == nd0: return True
    return False

if __name__ == '__main__':
    # Example 7

    # FRA accepting words a1 a2 ... such that ai != aj if i != j
    r = 1; n = 1
    mu = [[]]
    delta = [(0,(0,"GFresh"),0)]
    A1 = FRA(r,n,mu,delta,[])

    FRA.resetAll()

    phi_ALLFresh = '(νX(). ⋀x. [x](X() ∧ (νY(). ⋀y. [y](Y() ∧ [x≠y]))()))()'
    t = parse_formula(phi_ALLFresh)
    t = AST(t)
    env = Environment()
    f = Formula.fromAST(t, env)
    depths = env.alternationDepths()
    c = Configuration(0,1)
    A1.check_configuration(c)
    G = FRAParity.build(A1,c,f,depths)
    # L = G.getLines()
    L = G.parity_game_lines()
    # for l in L: print(*l)
    # print(L)
    output = parity_game_solver(L)
    print(f"Out: {output['stdout']} \n\nError: {output['stderr']} \n\nExit Code: {output['exit_code']}")
    print("Defender won:", did_defender_win(output['stdout']))
