from re import *
print(sub(r"([B-DF-HJ-NPR-TV-XZb-df-hj-npr-tv-xz0-9\W_]*)([aeyuio])([B-DF-HJ-NPR-TV-XZb-df-hj-npr-tv-xz0-9\s]*)([aeyuio])(\w*)", r"\1\4\3\2\5", input()))
