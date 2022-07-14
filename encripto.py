import math
s= None
s='feedthedog'
raiz=math.sqrt(len(s))
red_bajo = math.floor(raiz)
red_alto = math.ceil(raiz)
mat=[]
matr = []
sal = []

if (red_bajo*red_alto)>= len(s):
    cont = 0
    for i in range(red_bajo):
        matr.append([])
        for j in range(red_alto):
            try:
                matr[i].append(s[cont])
                cont += 1
            except:
                pass
    for j in range(red_alto):
        for i in range(red_bajo):
            try:
                aux = list(matr[i])
                mat.append(aux[j])
            except:
                pass
else:
    red_bajo=red_bajo + 1
    cont = 0
    for i in range(red_bajo):
        matr.append([])
        for j in range(red_alto):
            try:
                matr[i].append(s[cont])
                cont += 1
            except:
                pass
            
    for j in range(red_alto):
        for i in range(red_bajo):
            try:
                aux = list(matr[i])
                mat.append(aux[j])
            except:
                pass
cont=0
for elem in mat:
    if cont < red_alto:
        sal.append(elem)
        cont +=1 
    else:       
        sal.append(' ')
        sal.append(elem)
        cont = 1
        
print("".join(sal) )
    
print(matr)

