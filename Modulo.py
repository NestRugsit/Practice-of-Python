x = int(input())
y = int(input())
i = 1
while i <= x :
  mod = i % y
  if mod == 0 :
    print(i)
  i+=1