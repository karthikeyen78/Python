N = int(input())

for i in range(N):
    current_char = chr(ord('A') + i)
    for j in range(i+1):
        print(current_char, end="")
        current_char = chr(ord(current_char) + 1)
    print()
