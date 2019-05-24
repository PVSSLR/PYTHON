import random

a = random.sample(range(10),5);
b = random.sample(range(10),7);
c = [];
for i in a:
 if i in b:
         c.append(i);

print(c);

