from enum import unique

name_1 = input('First name : ').lower()
name_2 = input('Second name : ').lower()
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
i=0
while True:
    if name1_list[i] in name2_list:
        name2_list.remove(name1_list[i])
        name1_list.pop(i)

    #    i = i - 1
    else:
        i = i + 1
    if len(name1_list) == i :
        break

flames_cnt = len(name1_list) + len(name2_list)
unique_letter = name1_list + name2_list
print(unique_letter)
print(flames_cnt)
flames = ['Friends','Lover','Affection','Marriage','Enemy','Siblings']
flames_new = list()
while True:
    if len(flames) == 1:
        print(flames)
        break
    if flames_cnt > len(flames):
        while True:
            flames_new = flames_new + flames
            if len(flames_new) >= flames_cnt:
                break
        popped = flames_new.pop(flames_cnt - 1)
        popped_idx = flames.index(popped)
        flames.remove(popped)
        flames = flames[popped_idx:] + flames[:popped_idx]
        flames_new.clear()
    else:
        popped = flames.pop(flames_cnt - 1)
        #popped_idx = flames.index(popped)
        #flames.remove(popped)
        flames = flames[flames_cnt - 1:] + flames[:flames_cnt - 1]