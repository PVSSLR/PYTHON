a = int(input("Enter the initial number: "))

y = []
for x in range(1,10):
  if a%x == 0:
     y.append(x)


print(y)
