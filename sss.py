import kbs
import copy
skills = [10, 10, 10, 10, 10]
ls = copy.deepcopy(kbs.VUZ6)
name = ls.pop(0)
ls.pop(0)
spisok = []
flag = 0
for activity in ls:
    for i in range(5):
        if skills[i] >= activity[2][i]:
            flag += 1
        else:
            flag = 0
    if flag == 5:
        spisok.append(activity[0:2])
    flag = 0
print(spisok)