arr=[396285104,573261094,759641832,819230764,364801279]
#arr=[1,2,3,4,5]
maxi=list()
cont=0
for item in arr:
    arr.remove(item)
    print(arr)
    maxi.append(sum(arr))
    arr.insert(cont, item)

    cont += 1
    print(maxi)
    

print(min(maxi), max(maxi))
