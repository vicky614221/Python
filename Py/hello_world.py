name_1 = input('First name : ')
name_2 = input('Second name : ')
name_1 = name_1.strip()
name_2 = name_2.strip()
name1_list = []
name2_list = []
for i in name_1:
    if i == ' ':
        continue
    else:
        name1_list.append(i)

for i in name_2:
    if i == ' ':
        continue
    else:
        name2_list.append(i)
for i in name1_list:
    for j in name2_list:
        if i == j:
            name1_list.remove(i)
            name2_list.remove(j)
            break
print(name1_list)
print(name2_list)
flames = ['Friend','Lover','Affectionate','Marriage','Enemy','Sister']
flames_cnt = len(name1_list) + len(name2_list)

if flames_cnt > 0:
    while len(flames)>0:
        (flames.pop((flames_cnt % len(flames)) - 1))
        if len(flames) == 1:
            print(flames)
            break
else:
    print('All letters are matching')




