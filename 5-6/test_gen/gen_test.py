import os
import shutil
from pathlib import Path

CURRENT_TASK = 'a'

if CURRENT_TASK == 'a':
    from a_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'b':
    from b_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'c':
    from c_test import TEST_CASES, get_test_string
if CURRENT_TASK == 'd':
    from d_test import TEST_CASES, get_test_string


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

        os.system(f"python solutions/sol_{CURRENT_TASK}.py < tests/{CURRENT_TASK}/{test_count} > temp_py.a")

        with open("temp_py.a") as file:
            py_ans = file.read()

        with open(f"tests/{CURRENT_TASK}/{test_count}.a", 'w') as file:
            file.write(py_ans)

        print(f"done {test_count} test")
        test_count += 1

if os.path.exists("temp_py.a"):
    os.remove("temp_py.a")
