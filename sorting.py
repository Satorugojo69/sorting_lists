fh =open('output.txt','w')

a = [9, 2, 1.5, 5, 8, 6, 4, 10]

fh.write("Before Sorting " + '\n')
fh.write(str(a) + '\n')


fh.write("After sorting" + '\n')
fh.write("Ascending " + '\n')
a.sort()
fh.write(str(a) + '\n')


fh.write("Descending" + '\n')
a.sort(reverse=True)
fh.write(str(a) + '\n')
fh.close