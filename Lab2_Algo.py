nums = [5, 7, 7, 8, 8, 10]
target = 10
start = -1
end = -1
i = 0

while i < nums.__len__():
    if nums[i] == target:
        if start == -1:
            start = i
            end = start
        else:
            end = i
    i += 1
print("[" + str(start) + ", " + str(end) + "]")
