
k =0
j = 0
max = 0
min = 10000000000000000000000000000

while k == 0  :
  i = int(input())

  if i < 0:
    break
  if   i > max:
    max = i
  if (i < min ):
    min = i
  
  
print("Max :",max)
print("Min :",min) 

