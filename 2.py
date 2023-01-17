# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open ('file2.txt', 'r') as data:
    file = ''.join(line.strip() for line in data)

lst_1, res_lst = file[0], ''

i = 0

for elem in file:
    if elem != lst_1[-1]:
        res_lst+= str(i) + lst_1[-1]
        i=1
        lst_1 = elem

    else:
        i+=1
        lst_1+=elem
res_lst+=str(i)+lst_1[-1]            

with open ('file3.txt', 'w') as data:
    data.writelines(res_lst)

with open ('file3.txt', 'r') as data:   
    file2 = ''.join(line.strip() for line in data)

res_lst = ''

for elem in file2:
    if elem.isalpha():
        elem = file2.index(elem)
        num = int(file2[0:elem])
        res_lst+=num*elem
        file2 = file2[elem+1:]

with open ('file4.txt', 'w') as data:
    data.writelines(res_lst)     

print(res_lst)    