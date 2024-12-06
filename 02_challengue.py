### Challengues ###

"FABONAZZI"

def fabonacci(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5  == 0:
        print("buzz")

for i in range(1, 101):
    if fabonacci(i) == None:
        print(i)
    else:
        print(fabonacci(i))