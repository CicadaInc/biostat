# def advice(age, gender):
#     stat = {}
#     with open('DATABASE.txt') as file:
#         for line in file.readlines():
#             date, value = line[4: line.find(':') - 1].replace('-', '.'), eval(
#                 line[line.find(':') + 2: -2])
#             if date not in stat:
#                 stat[date] = value
#             else:
#                 for i in range(4):
#                     stat[date][i] += value[i]
#     fats, proteins, carbohydrates, calories = 0, 0, 0, 0
#     for item in stat:
#         fats += stat[item][0]
#         proteins += stat[item][1]
#         carbohydrates += stat[item][2]
#         calories += stat[item][3]
#     print(fats, proteins, carbohydrates, calories)
#     many, few = [], []
#     if gender == 'man':
#         if age >= 18 and age <= 29:
#             if fats > 53:
#                 many.append('fats')
#             elif fats < 53




import socket
print(socket.gethostbyname(socket.gethostname()))