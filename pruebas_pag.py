def solution(S):
    num = 39878
    sal = None
    repetidos=[]
    x = [int(a) for a in str(num)]

    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                if x[i] == x[j] and x[i] not in repetidos:
                    repetidos.append(x[i])

    if len(repetidos) == 3:

        x.remove(repetidos[0])
        x.remove(repetidos[0])
        x.remove(repetidos[1])
        x.remove(repetidos[1])
        x.remove(repetidos[2])
        x.remove(repetidos[2])
        x.sort()
        sal=+(repetidos[0])+(repetidos[1]*10)+(repetidos[2]*100)+(x[-1]*1000)+(repetidos[2]*10000)+(repetidos[1]*100000)+(repetidos[0]*1000000)

    elif len(repetidos) == 2:

        x.remove(repetidos[0])
        x.remove(repetidos[0])
        x.remove(repetidos[1])

        x.remove(repetidos[1])
        x.sort()
        sal=+(repetidos[0])+(repetidos[1]*10)+(x[-1]*100)+(repetidos[1]*1000)+(repetidos[0]*10000)

    elif len(repetidos) == 1 and repetidos[0] != 0:

        x.remove(repetidos[0])
        x.remove(repetidos[0])
        x.sort()
        sal=(repetidos[0])+(x[-1]*10)+(repetidos[0]*100)
        
    elif len(repetidos) == 1:
        
        x.sort()
        sal = x[-1]
        
    else:
        x.sort()
        sal = x[-1]

    return sal


print(solution(39878))
