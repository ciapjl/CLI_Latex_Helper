import unittest
import sys

sys.path.append('/home/jean-luc/Documents/OdinProject/Python_CLI/CLI_Latex_Helper/')


from utils.integrals import processIntegral



class testIntegralParser(unittest.TestCase):

    def test_simpleIntegral(self):
        output = processIntegral("4x dx", "1 2")
        text = "`4x dx` and `1 2` shoudl give integral of 4x dx from 1 to 2"
        expectedOutput = '\[\int{_{1}^{2}}{4x \ dx}\]'
        self.assertEqual(output, expectedOutput,text)

    def test_ambiguousVariableOfIntegration(self): 
        output = processIntegral("3", "45, 67")
        text = "`3` and `45, 67` shoudl give integral of 3 dt from 45 to 67"
        expectedOutput = '\[\int{_{45}^{67}}{3 \ dt}\]'
        self.assertEqual(output, expectedOutput,text)

    def test_needVariableOfIntegrationAdded(self):
        output = processIntegral("4a+6a^2+43a^3", "-2x, 2x+1/2")
        text = "`4a+6a^2+43a^3` and `-2x, 2x+1/2` shoudl give integral of  from -2x to 2x+1/2"
        expectedOutput = '\[\int{_{-2x}^{2x+1/2}}{4a+6a^2+43a^3 \ da}\]'
        self.assertEqual(output, expectedOutput,text)


if __name__ == '__main__':
    unittest.main()