print('Begin program')
print('***************')

fhand   =   open("sample.txt")

for i in fhand:
    print(i.strip())
    #for j in i:
    #    print(j)
