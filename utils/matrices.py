import re


BACKSLASH = chr(92)



matrix_description = "This options adds the ability to typset matrices. The content of the matrix(i.e. its entries) will be added using the main INPUT channel, with values/entries delineated with the following set of symbols(or similar): ,;| . The option can be used to specify the dimension of the relevant size of the matrix where the convention is rows*columsn. By default, the entries will be filled from left to right, starting with the top row. For instance to 2 by 2 matrix with values (a,b,c,d) where a c form the usual diagonal, and b,d form the opposite diagonal, the command should read: 'a,b,c,d'  --matrix '2*2'. If None appears in the final output of the matrix, it means the input is poorly formed and was unabled to be parsed(either because of some logical error, such as the fact that the dimensionality of the matrix does not match the number of entries, or because the input was not comprehensible) "

BACKSLASH = chr(92)



def processMatrixDimensions(dimensions):
    dimension_array = re.split("[,;*| ]", dimensions)
    dimension_array = list(filter(lambda x: x != '', dimension_array))
    if len(dimension_array) != 2:
        return None
    else:
        dimension_array = [int(x) for x in dimension_array]
        return (dimension_array[0], dimension_array[1])
        
    
print(processMatrixDimensions("2,2"))

    
def processMatrixEntries(input, dimensions):
    outputEntries = ""
    entries_array  = re.split("[,;*| ]", input)
    entries_array = list(filter(lambda x: x != '', entries_array))
    processDimensions = processMatrixDimensions(dimensions)
    if processDimensions == None:
        return None
    nRows, nCols = tuple(processMatrixDimensions(dimensions))
    if nRows*nCols != len(entries_array):
        return None
    i = 0
    while nRows > 0:
        for x in range(nCols):
            atlastEntryInRow = (x == (nCols -1))
            if atlastEntryInRow:             
                outputEntries = f"{outputEntries}{entries_array[i+x]}{BACKSLASH}{BACKSLASH}\n"
            else:
                outputEntries = f"{outputEntries}{entries_array[i+x]} & "
        i += nCols
        nRows -= 1

    return outputEntries

def processMatrix(input, dimensions):
    entries = processMatrixEntries(input, dimensions)
    return f"{BACKSLASH}{{pmatrix}}\n{entries}{BACKSLASH}{{pmatrix}}"
