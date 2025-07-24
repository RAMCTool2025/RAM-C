import xml.etree.ElementTree as ET
from DataStructures.FRA import *
# from DataStructures.CommonTypes import *

# Function to add an element to the dictionary, where the value is the number of items in the dictionary.
# This allows normalised renaming of states / registers



def add_element(original, renamed_dict):
    if original in renamed_dict: return renamed_dict[original]
    value = len(renamed_dict)
    renamed_dict[original] = value
    return value

# Parses an XML file containing the specification of an FRA.
def parse_xml(filename: str) -> tuple[int, int, list[list[Register]], list[Transition], list[State], list[Tag]]:
    tree = ET.parse(filename)
    root = tree.getroot()

    known_alias = ["Known", "Stored", "Read"]

    state_renamed = {}
    register_renamed = {}
    delta = []
    q_fin = []
    initial_state = root.find('initial-state').text
    add_element(initial_state, state_renamed)

    # Parse states
    all_states = root.find('states').findall('state')
    n = len(all_states) # number of states can be obtained here
    mu = [set() for _ in range(n)] # mu can be setup in a fixed length
    for state in root.find('states').findall('state'):
        state_id = state.find('id').text
        state_value = add_element(state_id, state_renamed)

        # Parse available registers
        available_registers = state.find('available-registers')
        if available_registers is not None:
            for reg in available_registers.findall('register'):
                register_value = add_element(reg.text, register_renamed)
                mu[state_value].add(register_value)
        mu[state_value] = list(mu[state_value])

    # Parse available final states
    final_states = root.findall('final-state')
    if final_states is not None:
        for state in final_states:
            q_fin.append(state_renamed[state.text])


    # Parse transitions and obtain tags
    tags = set()
    for trans in root.find('transitions').findall('transition'):
        from_state = trans.find('from').text
        to_state = trans.find('to').text
        input_sym = trans.find('input')
        tag = None
        if input_sym is not None:
            tag = input_sym.text
            tags.add(tag)
        op = trans.find('op').text
        register = trans.find('register').text

        # Rename states using the mapping
        renamed_from = state_renamed[from_state]
        renamed_to = state_renamed[to_state]

        # Rename the register using the mapping
        if register not in register_renamed:
            register_renamed[register] = len(register_renamed)
        renamed_register = register_renamed[register]

        # Normalise the operation for Known and its alias's
        if op in known_alias:
            op = "Stored"

        # Add the transition to delta, removing the tag if it is not there
        if tag is not None:
            delta.append((renamed_from, (tag, renamed_register, op), renamed_to))
        else:
            delta.append((renamed_from, (renamed_register, op), renamed_to))
    if len(tags) == 0: tags = None
    else: tags = list(tags)
    r = len(register_renamed)  # obtain the number of registers

    return r, n, mu, delta, q_fin, tags


if __name__ == '__main__':
    test_FRA = FRA(*parse_xml("./FRA_Stack_1.xml"))
    print(test_FRA)