f1 = open('File_input1.txt', 'r')
f2 = open('File_input2.txt', 'r')
f3_sort = open('File_input3.txt', 'r')

for line1 in f1:
    for line2 in f2:
        if line1 == line2:
            f3_sort.write("%s\n" %(line1))

f3_sort.close()
f1.close()
f2.close()

