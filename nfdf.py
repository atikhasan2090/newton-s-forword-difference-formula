n = int(input("enter the number of dataset :"))

li = [[0 for i in range(n)]for i in range(n+1)]

for i in range(n):
    li[0][i] = int(input("enter the value of x{}  : ".format(i)))
    
for i in range(n):
    li[1][i] = int(input("enter the value of y{}  : ".format(i)))

x = int(input("enter the unknown value of x : "))

u = ( x - li[0][0] ) / ( li[0][1] - li[0][0] )

for i in range (n-1):
    for j in range(n-1-i):
        
        li[i+2][j] = li[i+1][j+1] - li[i+1][j]
        

y = li[1][0]

for i in range(n-1):
    temp_u = u
    su = 1
    for j in range(i+1):
        su = su*temp_u
        temp_u = temp_u-1
    
    fact = 1
    temp = 1
    for j in range(i+1):
        fact = fact*temp
        temp = temp + 1
    
    y = y + su * li[i+2][0] / fact



print(y)