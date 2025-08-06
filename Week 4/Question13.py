file = open('sum.txt', 'r')
nums = file.readlines()
y = 0

for row in nums:

    for elem in row.split():
        y+=int(elem)


print(y)
