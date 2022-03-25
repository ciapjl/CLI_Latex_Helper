#import outside libraries

import typer

#imports from other files with relevant functions

from  utils.integrals import processIntegral, integral_description



def main(input: str, integral: str = typer.Option("", help=integral_description)):
    if integral != "":
        typer.echo(processIntegral(input,integral))


if __name__ == '__main__':
    typer.run(main)
