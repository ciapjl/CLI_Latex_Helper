# CLI_Latex_Helper
Basic Latex Parser for things that may be cumbersome to typset, such as matrices and integrals. 

This CLI tool currently provides several options to tranform basic/quick "normal"(i.e. non latexed/typset) into latex typset. 

This is achieved is by separating the use cases into several options available at the CLI(which turn out to be the tool's features):

- equations
- integrals
- matrices

The CLI always takes a principal argument, termed `input` . As default, the tool returns a typset version of the `input` place by the user. 

In order to use the tool, the following command pattern is required after cloning this repository and cding into the relevant folder:

`python main.py "insert text here to be typset`

where "insert text here to be typset" corresponds to the `input` variable. It is crucial that the user uses quotes("") if they wish to insert any text that has spaces, otherwise the tool will attempt to read it as multiple arguments/options.

Additionally, the tool includes the flags above, whose functionality and instructions to use them will be explained under each heading.

### Equations

The `--equation` flag, used after the main input variable, gives the option for an equation to be typeset. Additionally, and more usefully, if the input contains multiple equations(and hence equation signs), each delineated with a comma, then the tool will automatically generate an align enviroment in which the system of equation is aligned. 

For instance, the command

`python main.py "5x+2=3y+12,2y+2=7" --equation`


gives us


```
\begin{align*}
 5x+2 &= 3y+12 \\
2y+2 &= 7
 \end{align*}
```



### Integrals

The integral flag, also used after the main input variable, gives the option for integrals to be typeset. However, the flag itself takes an argument, meaning that 

1. The `input` variable will be used as the content of the integral(i.e. the function being integrated/the integrand)
2. The `integral` flag/variable will specificy the bounds of the integral, which can be delimited using a space or comma(see following example)


For example, the command 

`python main.py "7dx" --integral "2,4"`

gives us

`\[\int{_{2}^{4}}{7 \ dx}\]`

The integral tool also has basic formatting and regex features where the relevant differential is added if omitted or implied, e.g. 

- `python main.py "2" --integral "a,b"` gives `[\int{_{a}^{b}}{2 \ dt}\]`
- `python main.py "4x^2+8x+2" --integral "-4,4"` gives `\[\int{_{-4}^{4}}{4x^2+8x+2 \ dx}\]`



### Matrices

Similar to the integral flag, the `--matrix` flag also takes an argument in addition to the main `input` argument supplied at the beginning. Indeed, the main `input` parameter will take a comma or space delimited list of the elements of the matrix/array. The argument supplied to the `--matrix` flag will specify the dimension of the matrix desired. 

For example, the command

`python main.py "a,b,c,d" --matrix "2*2"`

gives us 

```
\{pmatrix}
a & b\\
c & d\\
\{pmatrix}
```


and similarly 

`python main.py "a,b,c,d,e,f" --matrix "3*2"`

gives us 
```
\{pmatrix}
a & b\\
c & d\\
e & f\\
\{pmatrix}
```

Note that the tool does some basis checking for logical consistency between the dimensions requested and the number of elements supplied. If ever the `None` keyword appears in the output of a function, assume that something is wrong with the input and that the user should revisit these paragraphs to check on the way to input data here. They can also check the test folder provided to see further examples of use cases.



#### Possible extensions/features/improvememts to be made

- Could be made more user friendly, arguably complex enough to just learn latex format instead, which kind of defeats the purpose of the project.
- More complex equation handling.
- Automatic copying to clipboard of the output to use in another program to avoid awkward terminal highlighting and shift-control-c. *NOTE* a possible workaround:  it seems(without verifying closely) that this can already by piping the output to xclip on linux.
- Testing: 
    - Make testing actually compare latex output using some kind of OCR, instead of verifying strings output(which isn't actually what is needed since multiple differnt strings can be compiled to produce the same latex output)
    - Test directly at the CLI level, not just the functions underlying the CLI
- Other possible features involving tikz and predictable, simple diagrams like exat sequences in homological algebra.