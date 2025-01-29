### Regular Expressions ###

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros"

# Match
match = re.match("Esta es la lección", my_string, re.I)
if match:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

match = re.match("Esta es la lección", my_other_string)
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# Search
search = re.search("Lección", my_string, re.I)
if search:
    print(search)
    start, end = search.span()
    print(my_string[start:end])

# Findall
findall = re.findall("lección", my_string, re.I)
print(findall)

# Split
split_result = re.split(":", my_string)
print(split_result)

# Sub
sub_result = re.sub("[l|L]ección", "LECCIÓN", my_string)
print(sub_result)
sub_result = re.sub("Expresiones Regulares", "RegEx", my_string)
print(sub_result)

# Patterns
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "ferOfficial@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))


email = "ferOfficial@gmail.com.mx.es"
print(re.findall(pattern, email))