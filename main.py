# import outside libraries

import typer

# imports from other files with relevant functions

from utils.integrals import processIntegral, integral_description
from utils.equations import processEquation, equations_description


integralTyperOption = typer.Option("", help=integral_description)
equationTyperOption = typer.Option("", help=equations_description)
inLineOption = typer.Option(
    False, help='Add this option to generate an inline tex form')


def main(
input: str,
integral: str = integralTyperOption,
equation: str = equationTyperOption, 
inline=inLineOption):
    if integral != "":
        typer.echo(processIntegral(input, integral))

    elif equation != "":
        typer.echo(processEquation(input, equation))

    else:
        typer.echo(f"")




if __name__ == '__main__':
    typer.run(main)
