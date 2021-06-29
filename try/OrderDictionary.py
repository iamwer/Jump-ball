# from collections import OrderedDict
# d1 = OrderedDict()
# d1['a'] = 'A'
# d1['b'] = 'B'
# d1['c'] = 'C'
#
# d2 = OrderedDict()
# d2['b'] = 'B'
# d2['a'] = 'A'
# d2['c'] = 'C'
#
# d3 = OrderedDict()
# d3['a'] = 'A'
# d3['b'] = 'B'
# d3['c'] = 'C'
#
# print(d1==d2)
# print(d1==d3)
#
# # for k,v in d1.items():
# #     print(k,v)

               # Tuples - Кортежи. Новая тема.


# strings = ('str1', 'str2', 'str3')
# strings[0] = 'str0'

# person = ['John', 'Silver', 22]
# print(person)
# print(len(person))
# print(person[0])
# print(person[-1])
# person[0] = 'Bob'
# print(person)
#
# print(person.count())

# players = [('Carlsen', 1990, 2842), ('Caruana', 1992, 2822), ('Memedyarov', 1985,2801)]
# print(players[0])
#
# from collections import namedtuple
#
#
# player = namedtuple('Player', 'name age rating')
# players = [Player('Carlsen', 1990, 2842), Player('Caruana', 1992, 2822), Player('Memedyarov', 1985, 2801)]
# print(players[0])

# if True:
#     print('Indeed, true.')
#
# if 3 > 2:
#     print('3 is greater than 2')
#
# if 3 < 2:
#     print('3 is less than 2')
#
# is_admin = True
# if is_admin:
#     print("It's admin, look at him!")
#
# selected_character = input()
# if selected_character == 'Protos':
#     print('Protos is the most powerful race')
# elif selected_character == 'Zerg':
#     print('Zerg is the most weak race but it spreads like a plague')
# elif selected_character == 'Terrain':
#     print('Terrain is a race balanced between Zerg and Protos')
# else:
#     print("Hmm... it seems we have a new race")

# my_set = set()
# print(my_set)
# print(type(my_set))
#
# my_set.add(1)
# print(my_set)
#
# my_set.add(2)
# print(my_set)
#
# my_set.add('Hello')
# print(my_set)
#
# my_set.add('home')
# print(my_set)
#
# my_set.add(2)
# print(my_set)
#
# my_list = [1,1,1,1,2,2,2,2,2,3,3,3,4]
# s = set(my_list)
# print(s)
# print(len(s))
#
# print(1 in s)
# print(5 in s)
#
# print('home' in my_set)
#
# set1 = {1,2,3,4}
# set2 = {1,2,3,4,5}
#
# print(set2.issubset(set1))
# print(set2.issuperset(set1))
#
# set1 = {1,2,3}
# set2 = {4,5,6}
# print(set1.isdisjoint(set2))
#
# set1 = {1,2,3,4}
# set2 = {1,2,3,4,5}
# print(set3.set1.union)(set2)

# set1 = {0,1,2,3,4}
# set2 = {1,2,3,4,5}
# set3 = set1.difference(set2)
# set4 = set1.symmetric_difference(set2)
# print(set3)
# print(set4)
#
#
# set1.update(set2)
# print(set1)
#
# set1.remove(1)
# print(set1)
#
# set2.remove(5)
# print(set2)
#
# set2.add(5)
# print(set2)
#
# set1.discard(2)
# print(set1)
#
#
#
# set1.clear()
# print(set1)

# numbers = [1,2,3,4,5]
# for i in numbers:
#     print(i*i)

# for i in range(1,6):
#     print(i)

# for i in range(1,6):
#     if i % 2 == 0:
#         print(f'{i} четное')
#     else:
#         print(f'{i} нечетное')

# numbers = [1,3,5,7,9]
# for i, item in enumerate(numbers):
#     numbers[i] *=2
# print(numbers)
#
#
# afkll = 'sdaflldfsj'
# for l in afkll:
#     print(l)

#
# for _ in range(5):
#     print("Alarm!")
#
# person = ('John', 'Silver', 22)
# for item in person:
#     print(item)

# shop = ('orange', 22.6, '22 kg')
# for property in shop:
#     print(property)

# persons = [('John', 22, '54 kg'), ('Bob', 44, '60 kg'), ('Dave', 34, '70 kg')]
# for (name, age, weight) in persons:
#     print(f'{name} is {age} and {weight} for men')

# players = dict(Carlsen = 2842, Caruana = 2822, Mamedyarov = 2801)
# for item in players:
#     print(item)
# for item in players.items():
#     print(item)
#
# for k,v in players.items():
#     print(f'{k} has rating {v}')

# list1 = [2,4,-5,6,8,-2]
# list2 = [2,-6,8,3,5,-2]
#
# pairs = []
# for x in list1:
#     for y in list2:
# print(pairs)

# greeting = 'Hello, world'
# chars = []
# for l in greeting:
#     chars.append(l)
# print(chars)
#
# chars = [l for l in greeting]
# print(chars)
#
# chars = [l for l in 'bla-bla-bla']
# print(chars)
#
# chars = [l for l in 'aoflasdf']
# print(chars)
#
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# print(numbers)
# numbers = [n for n in range(0,11)]
# print(numbers)
#
# numbers = [n*n for n in range(0,11)]
# print(numbers)
#
# numbers = [n*n for n in range(0,11) if n%2!=0]
# print(numbers)
#
# len_in_centimeters = [12,10,54,124,64]
# len_in_centimeters = [(round(cm / 2.3,2)) for cm in len_in_centimeters]
# print(len_in_centimeters)
#
#
#
# list1 = [2,4,-5,6,-2]
# list2 = [2,-6,8,3,5,-2]
# pairs = []
# for x in list1:
#     for y in list2:
#         cur_sum = x + y
#         if cur_sum == 0:
#             pairs.append((x,y))
# print(pairs)
#
# pairs = [(x,y) for x in list1 for y in list2 if x+y==0]
# print(pairs)

x = 0
while x < 3:
    print(f'x equals {x}')
    x+=1
else:
    print('Condition is not met')

vals = [1,2,3,4,5,6,7,8,9]
sum = 0
for v in vals:
    if v % 2 == 0:
        continue
    else:
        sum+=v
    if sum > 10:
        break
print(sum)
