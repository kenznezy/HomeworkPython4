# 11
# Скопировать из файла F1 в файл F2 все строки, которые содержат только одно слово.
# Найти самое короткое слово в  файле F2.

file = open("F1.txt", "r")

lines = file.readlines()
file.close()

numoflines = 0
for line in lines:
    numoflines += 1

print("number of lines in file: "+str(numoflines))

print(lines)


reqlines = []
for i in range(0, numoflines):
    for j in range(0, len(lines[i])-1):
        if lines[i][j].isspace():
            lines[i] = " "
            break

print(lines)

for i in range(0, len(lines)-1):
    if lines[i].isspace():
        continue
    else:
        reqlines.append(lines[i])

print(reqlines)

file2 = open("F2.txt", "w")
file2.writelines(reqlines)
file2.close()


minlen = len(reqlines[0])
for i in range(0, len(reqlines)-1):
    if len(reqlines[i])<minlen:
        minlen = len(reqlines[i])
        minindex = i

print('smallest word in F2 is: '+str(reqlines[minindex]))