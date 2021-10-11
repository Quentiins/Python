x = int(input("Quelle est la valeur de x : "))
y = int(input("Quelle est la valeur de y : "))

temp_1 = x
x = y
y = temp_1

print(f"La valeur de x après avoir swap : {x}")
print(f"La valeur de y après avoir swap : {y}")
