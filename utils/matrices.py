import re


matrix_description = "This options adds the ability to typset matrices. The content of the matrix(i.e. its entries) will be added using the main INPUT channel, with values/entries delineated with the following set of symbols(or similar): ,;| . The option can be used to specify the dimension of the relevant size of the matrix where the convention is rows x columsn. By default, the entries will be filled from left to right, starting with the top row. For instance to 2 by 2 matrix with values (a,b,c,d) where a c form the usual diagonal, and b,d form the opposite diagonal, the command should be: 'a,b,c,d'  --matrix '2x2' "


def matrixTyperOption(input, dimensions):
    pass