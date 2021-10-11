x = int(input("Quelle est la valeur de x : "))
y = int(input("Quelle est la valeur de y : "))
z = int(input("Quelle est la valeur de z : "))

if x > y and x > z:
    print(f"x est plus grand que y et z")
elif y > z and y > z:
    print(f"y est plus grand que x et z")
elif z > x and z > y:
    print(f"z est plus grand que x et y")
else:
    print(f"Deux ou trois nombres sont égaux.")
