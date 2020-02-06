num = [int(x) for x in open('text.txt')]
print(num)
pNum = [x for x in num if x % 2 == 0]
print(pNum)