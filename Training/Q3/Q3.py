number = int(input("Enter a number:"))
l1 = list(range(1,number+1))
l2=[]
for i in l1:
    l2.append(pow(i,2))
dict = {k:v for k,v in zip(l1,l2)}
print(dict)