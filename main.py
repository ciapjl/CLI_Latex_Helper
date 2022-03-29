# import outside libraries

import typer

# imports from other files with relevant functions

from utils.integrals import processIntegral, integral_description
from utils.equations import processEquation, equations_description
from utils.matrices import processMatrix, matrix_description

integralTyperOption = typer.Option("", help=integral_description)
equationTyperOption = typer.Option("", help=equations_description)
matrixTyperOption = typer.Option("", help=matrix_description)


def main(
input: str,
integral: str = integralTyperOption,
equation: bool = False,
matrix: str = matrixTyperOption,
):
    if integral != "":
        typer.echo(processIntegral(input, integral))

    elif equation:
        typer.echo(processEquation(input))

    elif matrix != "":
        typer.echo(processMatrix(input, matrix))
    else:
        typer.echo(f"\[{input}\]")




if __name__ == '__main__':
    typer.run(main)
