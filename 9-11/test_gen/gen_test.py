import sys
import os
import shutil
from pathlib import Path

CURRENT_TASK = 'a'
COMPILER_PATH = "C:/mingw64/bin"
pyton_solution = True

if CURRENT_TASK == 'a':
    from a_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'b':
    from b_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'c':
    from c_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'd':
    from d_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'e':
    from e_test import TEST_CASES, get_test_string
    pyton_solution = False


test_count = 1
path = Path(os.getcwd())
parent_path = str(path.parent.absolute()).replace('\\', '/')
os.chdir(parent_path)
if not os.path.exists("tests"):
    os.mkdir("tests")
if os.path.exists(f"tests/{CURRENT_TASK}"):
    shutil.rmtree(f"tests/{CURRENT_TASK}")
if not os.path.exists(f"tests/{CURRENT_TASK}"):
    os.mkdir(f"tests/{CURRENT_TASK}")
for case, count in TEST_CASES:
    for i in range(count):
        with open(fr"tests/{CURRENT_TASK}/{test_count}", 'w') as file:
            file.write(get_test_string(*case.gen_case_common()))

        os.system(f"{COMPILER_PATH}/task_{CURRENT_TASK}.exe < tests/{CURRENT_TASK}/{test_count} > temp_cpp.a")
        if pyton_solution:
            os.system(f"python solutions/sol_{CURRENT_TASK}.py < tests/{CURRENT_TASK}/{test_count} > temp_py.a")

        with open("temp_cpp.a") as file:
            cpp_ans = file.read()
        if pyton_solution:
            with open("temp_py.a") as file:
                py_ans = file.read()

        if pyton_solution and cpp_ans.split() != py_ans.split():
            print("Py and cpp and are not same on test:")
            with open(f"tests/{CURRENT_TASK}/{test_count}") as file:
                print(file.read())
            print("py_ans:")
            print(py_ans)
            print("cpp_ans:")
            print(cpp_ans)
            sys.exit(1)
        else:
            with open(f"tests/{CURRENT_TASK}/{test_count}.a", 'w') as file:
                file.write(cpp_ans)

        print(f"done {test_count} test")
        test_count += 1
