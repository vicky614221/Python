print('Begin program')
print('***************')

fhand = open("sample.txt")
di = dict()
for line in fhand:
    line    =   line.strip()
    line_words   =   line.split()
    for each_words in line_words:
        di[each_words] = di.get(each_words,0) + 1

print(di)

bigcount = 0
bigword = None
for k,v in di.items():
    if v>bigcount:
        bigword = k
        bigcount = v

print(bigword)


print('***End of program***')
