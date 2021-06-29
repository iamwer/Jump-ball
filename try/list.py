# int_list = [1,2,3]
# print(int_list)
#
# mixed_list = [1,2.0,'string']
# print(mixed_list)
# print(len(int_list))
#
# print(int_list[2])
#
# print(int_list[-1])
#
# print(int_list[1:])
#
# names1 = ['John', 'Bod', 'Alice']
# names2 = ['Trace', 'Elijah', 'Mason']
# names_combine = names1 + names2
# print(names_combine)
#
# names1[0] = 'Liam'
# print(names1)
#
# names1.append('William')
# names1.append('Robert')
# names1.append('Tony')
# print(names1)
# print(sorted(names1))
#
#
# letter = ['ac','ab','aa']
# print(sorted(letter))
#
# letters = ['abc', 'a','ab']
# print(len(letters))

# numbers = [3,2,6,0,1,34,1]
#
# print(numbers.index(34))

players = {
            'Carlsen': 2842,
            'Caruana': 2822,
            'Mamedyarov': 2801,
            'Ding': 2797,
            'Giri': 2780
         }
print(players)

top1 = players['Carlsen']
print(top1)

players['So'] = 2780
print(players)

players['So'] = 2781
print(players)


print(type(players))

print('Carlsen' in players)
print('Kramnik' in players)
print(type(players))

players_copy = players.copy()
print(players_copy)

for k, v in players.items():
    print(k,v)

items = players.items()
print(type(items))

print(players.popitem())

print(len(players))

players.setdefault('Karjakin')
print(players)