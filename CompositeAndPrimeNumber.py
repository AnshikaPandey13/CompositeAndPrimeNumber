a=int(input("Range Start:-"))
b=int(input("Range End:-"))
for num in range (a,b+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is composite")
                break
        else:
                print(num,"is prime")
c,d=a,b
prime=0
composite=0
for num in range(c,d+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                composite+=1
                break
        else:
            prime=+1
print(prime,"Prime and",composite,"Composite numbers are there in the range.")