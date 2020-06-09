num = int(input("cuantos numeros perfectos desea ver?       "))
if num ==1:
    nu=10
if num ==2:
    nu=30
if num ==3:
    nu=500
if num ==4:
    nu=8200
if num ==5:
    nu=33550340
if num ==6:
    nu = 8589869060

for i in range(1, nu+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print(b)
