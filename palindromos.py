num = 12345
sal = None
repetidos=list()
aux = list()
ma=list()
x = [int(a) for a in str(num)]

for num in x:
    if num not in repetidos:
        repetidos.append(num)
    else:
        aux.append(num)
        repetidos.remove(num)
ma=str(max(repetidos))

sal=list(aux)+list(ma)+list(aux[::-1])

print(ma)
print(repetidos)
print(aux)
print(str(sal))

