def extraLongFactorials(n):
    
    if n == 0:
        fac=1
    else:
        fac = 1
        while(n > 1):
            fac = fac * n
            n = n-1
    print(fac)
    return fac

if __name__ == '__main__':
    n = int(input().strip())
    
    extraLongFactorials(n)
