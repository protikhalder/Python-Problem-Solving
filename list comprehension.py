lus = [1,2,3]
los = [1,2,3,4]
# TODO: all list 1 add for loop
new_list = []
for i in lus:
    add = i+1
    new_list.append(add)
# print(new_list)

# TODO: all list 1 add map lamda loop
blle = map(lambda x : x+1, lus)
# print(list(blle))

# TODO: all list 1 add map list comperhension
nw_list = [i+1 for i in los]


name = "Protuik"
new_list_name = [ i for i in name]
# print(new_list_name)


changelle = [i*2 for i in range(1,5)]
# print(changelle)

che = ['arger', 'brgewwrg', 'cefrgrger', 'Protik', 'errgreger', 'frgrgrgr', 'POLOKM']
print(che)
new = [i for i in che if len(che)<5]
print(new)