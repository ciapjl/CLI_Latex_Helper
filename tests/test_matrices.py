from concurrent.futures import process
import unittest
import sys

sys.path.append('/home/jean-luc/Documents/OdinProject/Python_CLI/CLI_Latex_Helper/')


from utils.matrices import processMatrix

BACKSLASH = chr(92)


class testMatrixParser(unittest.TestCase):


    def test_simplMatrix(self):
        output = processMatrix("a,b,c,d", "2*2")
        text = 'Test whether we get the basic 2 by 2 matrix with a c on the main diagonal'
        expectedOutput = f"{BACKSLASH}{{pmatrix}}\na & b{BACKSLASH}{BACKSLASH}\nc & d{BACKSLASH}{BACKSLASH}\n{BACKSLASH}{{pmatrix}}"
        self.assertEqual(output, expectedOutput,text)

   
    def testParsingErrorSizedNotWellDefined(self):
       output = processMatrix('a,b', "2*2" )
       text = 'Test whether we get a None result when the number of entries mismatches dimensions specified'
       expectedOutput = f"{BACKSLASH}{{pmatrix}}\nNone{BACKSLASH}{{pmatrix}}"
       self.assertEqual(output, expectedOutput,text)

    def test_NonSquareMatrix(self):
        output = processMatrix("a,b,c,d,e,f", "3*2")
        text = 'Test whether we get the basic 2 by 2 matrix with a c on the main diagonal'
        expectedOutput = f"{BACKSLASH}{{pmatrix}}\na & b{BACKSLASH}{BACKSLASH}\nc & d{BACKSLASH}{BACKSLASH}\ne & f{BACKSLASH}{BACKSLASH}\n{BACKSLASH}{{pmatrix}}"
        self.assertEqual(output, expectedOutput,text)

    def test_LargeMatrix(self):
        output = processMatrix("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16", "4*4")
        text = 'Test whether we get the basic 2 by 2 matrix with a c on the main diagonal'
        expectedOutput = f"{BACKSLASH}{{pmatrix}}\n1 & 2 & 3 & 4{BACKSLASH}{BACKSLASH}\n5 & 6 & 7 & 8{BACKSLASH}{BACKSLASH}\n9 & 10 & 11 & 12{BACKSLASH}{BACKSLASH}\n13 & 14 & 15 & 16{BACKSLASH}{BACKSLASH}\n{BACKSLASH}{{pmatrix}}"
        self.assertEqual(output, expectedOutput,text)







if __name__ == '__main__':
    unittest.main()