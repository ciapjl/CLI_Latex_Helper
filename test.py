import re

txt = "x,y,    2,3;3"
x = re.split("[, *;-]", txt)
x = list(filter(lambda x: x !='', x))
print(x) 