import os
import unittest

import ast
from pathlib import Path
import sys
import unittest
import json

from proc import run, run_flake8

TIMEOUT = 15  # seconds
ENCODING = 'UTF8'
TARGET_FILE = 'Test_Code/trig.py'

with open("testvalues.json") as fh:
    tests = json.load(fh)["TRIG"]

TESTS = [x for x in tests]



def setScore(score,player):
        with open("savestate.json","r") as fh:
            p = json.load(fh)
        with open("savestate.json","w") as fh:   
            p["coins"] += score
            json.dump(p,fh)

if os.environ.get('GS_LOCAL') == 'true':
    print("Running locally...")
    results_path = 'results.json'
else:
    results_path = 'results.json'


class TestTrig(unittest.TestCase):
   
    player = ""
    target_file = TARGET_FILE
    target_present = False
    test_procs = []


    @classmethod
    def setUpClass(cls):
        
        """This is run once to initialize class. """
        cls.target_file_present = Path(cls.target_file).is_file()
        if cls.target_file_present:
            for test in TESTS:
                cls.test_procs.append(run(cls.target_file))

    def setUp(self):
        """This is run before each test. """
        self.score = 0
        if not self.target_file_present:
            self.fail('Target file ' + self.target_file + ' not found! '
                      'File should be named ' + self.target_file + '.')


    def test_docstring_present(self):
        """Verify docstring is present (element_lookup.py). """
        with open(self.target_file, 'r') as fh:
            tree = ast.parse(fh.read())
        docstring = ast.get_docstring(tree)
        self.player = docstring
        print(docstring)
        self.assertIsNotNone(docstring)

    def test_rec(self):
        '''
        for i,pr in enumerate(self.sqrt_procs):
            output = pr.stdout
            output.lower()

        
            expected = SQRT_TESTS[i][1]
            actual = output

            if actual.find(expected) != -1:
                setScore(1,self.player)
            else:
                print(f"Expected to find '{expected}' in response "
                      f"(case-insensitive). \n"
                      f"Actual: {actual}")'''
        num = 3
        try:
            import Test_Code.recaman as rec
        except ImportError:
            return
        for i in range(num):
            expected = TESTS[i][1]
            actual = rec.next_recaman(TESTS[i][0])
            if expected == actual:
                setScore(1,self.player)



    '''def test_no_magic_numbers(self):
        """Verify that there is no magic number (element_lookup.py). """
        with open(self.target_file, 'r') as fh:
            tree = ast.parse(fh.read())
            constants = [x for x in ast.walk(tree)
                         if isinstance(x, ast.Constant)]
            for constant in constants:
                if constant.value in [116, 117, 118, 119, 120]:
                    print(f"I see a magic number "
                          f"in your code ({constant.value}).")'''


    '''def test_invalid_input(self, set_score):
        score = 0

        for i, proc in enumerate(self.opt_procs):  # iterate through runs
            output = proc.stdout.split(': ')
            output = [s.lower() for s in output]

            expected = OPT_TESTS[i][2][0]
            actual = output[-1]

            if actual.find(expected) != -1:
                score += weight_ / len(self.num_procs)
            else:
                print(f"Expected to find '{expected}' in response "
                      f"(case-insensitive). \n"
                      f"Actual: {actual}")'''

    def test_return_code(self):
        """Verify program runs without error (element_lookup.py). """
        ok_count = 0
        score = 0
        all_procs = self.test_procs
        for proc in all_procs:
            if proc.returncode == 0:
                score += 1
                ok_count += 1
            else:
                print("Test failed with non-zero exit code.", file=sys.stderr)
                # TODO Maybe a little explanation is in order (e.g., failed on 999)
        if ok_count == len(all_procs):
            print('Program runs without raising errors. Return codes all 0.')
        else:
            print('Only ' + ok_count + ' tests ran successfully.')

        setScore(score,self.player)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    #with open(results_path, 'w') as fh:
    unittest.main()