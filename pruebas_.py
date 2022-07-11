import re

name = input("Enter file:")

if len(name) < 1:
    name = "regex_sum_42.txt"
try: 
    handle = open(name)

except:
    print('chingao')
    quit()

count=dict()
nums = 0
for line in handle:
    i=0
    line=line.strip()
    num = re.findall('[0-9]+',line)
    if len(num) != 0:        
        for nu in num: 
            nums=nums+int(num[i])    
            i=i+1

print(nums)


            
            

    
