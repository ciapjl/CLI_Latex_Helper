import re

equations_description = 'add equation using the equation option '

BACKSLASH = chr(92)









def processEquation(input):
    #if more than one equal - call aligned function to take care of 
    eqnEnviron = ""
    if input.count('-') > 1:
    #else process here 
        pass
    else:
        eqnEnviron = f"{BACKSLASH}begin{{equation}} \n {input} \n {BACKSLASH}end{{equation}}"
    return eqnEnviron




# def processAlignedEquations(input):
# """This function helps process systems of equations, or those that need to done over multiple lines"""
