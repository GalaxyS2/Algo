A = [23171, 21011, 21123, 21366, 21013, 21367]
n = 6
profit = 0

for i in range(0, n, 1):
    for j in range(i + 1, n, 1):
        if A[j] - A[i] > profit:
            profit = A[j] - A[i]

print(profit)
