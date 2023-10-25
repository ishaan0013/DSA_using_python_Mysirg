lst = [0, 1]
N = int(input("Enter number of terms:\n"))

for i in range(0, N):
    sum = lst[i]+lst[i+1]
    lst.append(sum)

print(lst)
