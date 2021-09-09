#LISTA
pares = []
for num in range(0, 101):
    if num % 2 == 0:
        pares.append(num)

print(pares)


#Es azucar sintactica, en hacer el codigo mas legible
 
#LIST COMPREHENSION
even = [num for num in range(1, 101) if num % 2 == 0]
print(even)



#DICCIONARIOS
cuadrados = {}

for num in range(1, 16):
    cuadrados[num] = num**2

print(cuadrados)

#DICTOINARY COMPREHENSION
squares = {num: num**2 for num in range(1, 16)}

print(squares)
