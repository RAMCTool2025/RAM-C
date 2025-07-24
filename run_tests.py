import runpy
import os
import sys

special_formulas = {"SUT.muhml", "Stack_2.muhml"}
special_FRAs = {"Example_8.xml", "2_Stack.xml"}

for a_filename in os.listdir("./tests/FRA"):
    if a_filename in special_FRAs or a_filename == "new": continue
    for f_filename in os.listdir("./tests/muHML"):
        if f_filename in special_formulas  or f_filename == "new": continue
        print(f"Testing Automata {a_filename[:-4]} with Formula {f_filename[:-6]}")
        sys.argv = ["", f"./tests/FRA/{a_filename}", f"./tests/muHML/{f_filename}"]
        runpy.run_path("run.py")
        print("*" * 50, "\n")

for a_filename in special_FRAs:
    for f_filename in special_formulas:
        print(f"Testing Automata {a_filename[:-4]} with Formula {f_filename[:-6]}")
        sys.argv = ["", f"./tests/FRA/{a_filename}", f"./tests/muHML/{f_filename}"]
        runpy.run_path("run.py")
        print("*" * 50, "\n")
