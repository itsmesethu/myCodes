n=int(input())
j=1
m=n-1
for i in range(n):
  print(" "*m,end='')
  print("*"*j)
  m=m-1
  j=j+2
