from glob import glob

nbfiles = glob("*.ipynb")

with open("tests.py","w") as f:
    f.write("""\
import sys,os
sys.path.append(os.getcwd())
from nbtest import _notebook_run

print("Running Notebooks...")
\n\n""")

for i, nb in enumerate(filter(lambda f:  not "Errors" in f,nbfiles)):  
    with open("tests.py", "a") as f:
        f.write(f"def test_ipynb_{i}():\n")
        f.write(f"\t nb, errors = _notebook_run('{nb}')\n")
        f.write("\t assert errors == []\n\n")
