f1 = open('File_input1.txt', 'r')
f2 = open('File_input2.txt', 'r')
f3_sort = open('Совпадающие ссылки.txt', 'w')
f4_sort = open('Несовпадающие ссылки.txt', 'w')

for line1 in f1:
    
    for line2 in f2:
        line3 = line1.replace('!','')
        line4 = line2.replace('!','')
        if line3 == line4:
            f3_sort.write("%s"%(line2))
            break
    else:
        f4_sort.write("%s"%(line1))
    f2.seek(0)

for line2 in f2:
    f1.seek(0)
    for line1 in f1:
        line3 = line1.replace('!','')
        line4 = line2.replace('!','')
        if line3 == line4:
            break
    else:
        f4_sort.write("%s"%(line2))

        
f1.close()
f2.close()
f3_sort.close()
f4_sort.close()
