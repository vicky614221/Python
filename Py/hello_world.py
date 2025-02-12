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

for cnt in range(len(name1_list)):
    break_flag_yes = False
    for i in name1_list:
        for j in name2_list:
            if i == j:
                name1_list.remove(i)
                name2_list.remove(j)
                break_flag_yes = True
                break
        if break_flag_yes:
            break
flame_cnt = len(name1_list) + len(name2_list)
flames = ['Friend','Lover','Affection','Marriage','Enemy','Sister/Brother']

if flame_cnt > 0:
    while len(flames) > 1:
        flames.pop(flame_cnt-1)
        continue
else:
    print('All letters are matching')
print(flames)





