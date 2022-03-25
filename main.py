from  integrals import processIntegral, integral_description
import typer
import re



def main(input: str, integral: str = typer.Option("", help=integral_description)):
    if integral:
        if " " in integral:
            a, b = integral.split(",")
        typer.echo(processIntegral(input,a,b))


if __name__ == '__main__':
    typer.run(main)
