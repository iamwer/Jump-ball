
# list = []
#
# Your_bottom = int(input())
# for i in range(1, Your_bottom+1):
#     list.append("*"*i)
# print(list[i-1])

# x = int(input())
# for i in range(1, x+1):
#     if i%2 ==0:
#         print(f'Число {i} четное')
#     else:
#         print(f'Число {i} не четное')


rows = int(input('Enter the number of rowa'))
for x in range(rows):
    print('*' * (x + 1))


limit = int(input('Enter the limit'))
for x in range(limit):
    if x %2 ==0:
        print(f'{x} is EVEN')
    else:
        print(f'{x} is ODD')
