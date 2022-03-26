#import outside libraries

import typer

#imports from other files with relevant functions

from  utils.integrals import processIntegral, integral_description
from utils.equations import processEquation, equations_description


def main(input: str, integral: str = typer.Option("", help=integral_description), equation: str = typer.Option("", help=equation_description)):
    if integral != "":
        typer.echo(processIntegral(input,integral))

    elif equation !="":
        typer.echo(processEquation(input,equation) )
    
    else:
        typer.echo(f"\[{input}\]")

    

    


if __name__ == '__main__':
    typer.run(main)
