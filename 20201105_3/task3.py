from re import *
print(sub(r"(0*[1-9]+0+)([1-9]+)(0+)([1-9]+)(\d*)", r"\1\4\3\2\5", input()))