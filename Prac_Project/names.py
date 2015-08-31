import itertools

name2 = ['et', 'at', 'as']
name1 = ['S', 'D', 'R']

new_list = list(itertools.product(name1, name2))

m = []
for i in new_list:
    m.append(i[0]+i[1])
print m
