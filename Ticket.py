a = [0, 0, 0]  # List to store counts of elements modulo 3

n = int(input())  # Input the number of elements

# Loop through the input elements
for _ in range(n):
    x = int(input())  # Input each element
    a[x % 3] += 1  # Increment the count of elements modulo 3

# Calculate the maximum number of pairs
print(a[0] // 2 + min(a[1], a[2]))

