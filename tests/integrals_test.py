import unittest

from utils.integrals import processIntegral



class integralTest(unittest.TestCase):

    def simpleIntegral(self):
        output = processIntegral("4x dx", "1 2")
        text = "`4x dx` and `1 2` shoudl give integral of 4x dx from 1 to 2"
        expectedOutput = '\[\int_{1}^{2}{4x \ dx}\]'
        self.assertEqual(output, expectedOutput,text)

    def ambiguousVariableOfIntegration(self): 
        output = processIntegral("3", "45, 67")
        text = "`3` and `45, 67` shoudl give integral of 3 dt from 45 to 67"
        expectedOutput = '\[\int_{45}^{67}{3 \ dt}\]'
        self.assertEqual(output, expectedOutput,text)

    def needVariableOfIntegrationAdded(self):
        output = processIntegral("4a+6a^2+43a^3", "-2x, 2x+1/2")
        text = "`4a+6a^2+43a^3` and `-2x, 2x+1/2` shoudl give integral of  from -2x to 2x+1/2"
        expectedOutput = '\[\int_{-2x}^{2x+1/2}{4a+6a^2+43a^3 \ da}\]'
        self.assertEqual(output, expectedOutput,text)
