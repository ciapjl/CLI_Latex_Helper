from concurrent.futures import process
import unittest
import sys

sys.path.append('/home/jean-luc/Documents/OdinProject/Python_CLI/CLI_Latex_Helper/')


from utils.equations import processEquation

BACKSLASH = chr(92)


class testEquationParser(unittest.TestCase):

    pass

    def test_simplEquation(self):
        output = processEquation("45x = 6y")
        text = "`45x = 6y` and `1 2` should give equation env with one line corresponding to 45x = 6y in the middle"
        expectedOutput = f"{BACKSLASH}begin{{equation}} \n 45x = 6y {BACKSLASH}{BACKSLASH}\n {BACKSLASH}end{{equation}}"
        self.assertEqual(output, expectedOutput,text)

    def test_alignEquationEasy(self):
        output = processEquation("2x+a=y,4y=3x")
        text = "Expected input '2x+a=y,4y=3x' to be given align with aligned = signs"
        expectedOutput = f"{BACKSLASH}begin{{align*}}\n 2x+a &= y {BACKSLASH}{BACKSLASH}\n4y &= 3x {BACKSLASH}{BACKSLASH}\n {BACKSLASH}end{{align*}}"
        self.assertEqual(output, expectedOutput,text)
        


    def test_alignEquationHard(self):
        output = processEquation("2x+4s=4ys, 4ab=2ax, 8q=   23xs")
        text = "Expect input '2x+4s=4ys, 4ab=2ax, 8q=   23xs' to be given align env with aligned = signs"
        expectedOutput = f"{BACKSLASH}begin{{align*}}\n 2x+4s &= 4ys {BACKSLASH}{BACKSLASH}\n4ab &= 2ax {BACKSLASH}{BACKSLASH}\n8q &= 23xs {BACKSLASH}{BACKSLASH}\n {BACKSLASH}end{{align*}}"
        self.assertEqual(output, expectedOutput, text)
    

if __name__ == '__main__':
    unittest.main()