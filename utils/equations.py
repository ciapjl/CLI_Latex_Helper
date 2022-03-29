import re

equations_description = 'add equation using the equation option '

BACKSLASH = chr(92)


def processAlignedEquations(input):
    """This function helps process systems of equations, or those that need to done over multiple lines"""
    alignEnviron = ""
    equations_array = re.split("[,;|.]", input)
    equations_array = list(filter(lambda x: x !='', equations_array))
    insideAlignEnv =  '\n'.join([x.replace(" ", "").replace('=', " &= ").strip() for x in equations_array])
    return f"{BACKSLASH}begin{{align*}}\n {insideAlignEnv}\n {BACKSLASH}end{{align*}}"




def processEquation(input):
    #if more than one equal - call aligned function to take care of 
    eqnEnviron = ""
    if input.count('=') > 1:
        return processAlignedEquations(input)
    else:
        eqnEnviron = f"{BACKSLASH}begin{{equation}} \n {input} \n {BACKSLASH}end{{equation}}"
    return eqnEnviron




