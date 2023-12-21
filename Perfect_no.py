#Python code to find perfect numbers from 1 to 1000
num = 1000
for i in range(1, num):
       if num % i == 0:
           print(i)
