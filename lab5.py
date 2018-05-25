a = list(map(int, input().split())) #ввід даних

i = 0
count = 0

while i < len(a):
    if abs(a[i+1]-a[i]) == 1:       #перевірка чи пара вже разом
        del a[i]
        del a[i]
    else:
        j = i + 1
        while j < len(a):
            if abs(a[i]-a[j]) == 1: #просес пересідання
                temp = a[i+1]
                a[i+1] = a[j]
                a[j] = temp
                count += 1
            j += 1
        i += 2
print(count)                        #вивід даних