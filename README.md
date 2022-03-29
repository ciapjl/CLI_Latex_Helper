# CLI_Latex_Helper
Basic Latex Parser for things that may be cumbersome to typset, such as matrices and integrals. 

This CLI tool currently provides several options to tranform basic/quick "normal"(i.e. non latexed) into latex typset. 

This is achieved is by separating the use cases into several options available at the CLI(which turn out to be the tool's features):

- equations
- integrals
- matrices

The CLI always takes _(1)_ - a principal argument  when the tool is called. As default, the



## Possible extensions/features/improvememts to be made

- Could be made more user friendly, arguably complex enough to just learn latex format instead, which kind of defeats the purpose of the project.
- More complex equation handling.
- Automatic copying to clipboard. NOTE a workaround:  it seems(without verifying closely) that this can already by piping the output to xclip on linux.
- Testing: 
    - Make testing actually compare latex output using some kind of OCR, instead of verifying strings output(which isn't actually what is needed since multiple differnt strings can be compiled to produce the same latex output)
    - Test directly at the CLI level, not just the functions underlying the CLI