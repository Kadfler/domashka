# # #Списки
# #
# # # #задание 1
# # # list1 = [1,2,3,4,5]
# # # print(list1)
# # #
# # # #задание 2
# # # list2 = [1,2,3,4,5]
# # # print(list2[0])
# # # print(list2[2])
# # # print(list2[4])
# # #
# # # #задание 3
# # # list3 = [1,2,3,4,5]
# # # list3[2] = 7
# # # print(list3)
# # #
# # # #задание 4
# # # list4 = []
# # # list4.append(3)
# # # list4.append(2)
# # # list4.append(1)
# # # print(list4)
# # #
# # # #задание 5
# # # list5 = [1,2,3,4,5]
# # # list5.pop(3)
# # # print(list5)
# # #
# # # #задание 6
# # # list6 = [1,2,3,4,5]
# # # sum = sum(list6)
# # # average = sum/len(list6)
# # # print(sum)
# # # print(average)
# # #
# # # #задание 7
# # # list7 = ["hello","world"]
# # # user_input = input("введите слово:")
# # # if user_input in list7:
# # #   print(True)
# # # else:
# # #   print(False)
# # #
# # # #задание 8
# # # list8 = [1,4,2,43,5]
# # # list8.sort()
# # # print(list8)
# # # list8.sort(reverse=True)
# # # print(list8)
# # #
# # # #задание 9
# # # list9 = [1,2,3,4,5]
# # # listTo3 = list9[:3]
# # # print(listTo3)
# # # last3list = list9[-3:]
# # # print(last3list)
# # # listEven = list9[::2]
# # # print(listEven)
# # #
# # # #задание 10
# # # list10 = [1,2,3,4,5]
# # # list11 = [6,7,8,9,10]
# # # listsum1 = list10 + list11
# # # print(listsum1)
# # # listsum2 = []
# # # listsum2.extend(list11)
# # # listsum2.extend(list10)
# # # print(listsum2)
# #
# # #Кортежи
# #
# # #задание 1
# # tuple1 = (123, 234, "Hello, World!", True, False)
# # print(tuple1)
# #
# # #задание 2
# # tuple2 = (123, 234, "Hello, World!", True, False)
# # print(tuple2[1], tuple2[3], tuple2[4])
# #
# # #задание 3
# # tuple3 = (123, 234, "Hello, World!", True, False)
# # print(tuple3[-1], tuple3[-2],)
# #
# # #задание 4
# # tuple4 = (123, 234, "Hello, World!", True, False, True, True)
# # print(tuple4.count(True))
# #
# # #задание 5
# # tuple5 = (123, 234, "Hello, World!", True, False)
# # print(tuple4.index(123))
# #
# # #задание 6
# # tuple6 = (123, 234, "Hello, World!", True, False)
# # print(tuple6[:3], tuple6[-3:], tuple6[::2])
# #
# # #задание 7
# # tuple7 = (123, 234)
# # tuple8 = ("Hello, World!", True, False)
# # tuplesum = tuple7 + tuple8
# # print(tuplesum)
# #
# # #задание 8
# # tuple8 = (123, 234, 567)
# # tuple8x3 = tuple8*3
# # print(tuple8x3)
# #
# # #задание 9
# # list11 = [1, 2, 3]
# # tuple9 = tuple(list11)
# # print(list11, tuple9)
# #
# # #задание 10
# # tuple10 = [1,2,3,4,5,6,7,8,9,0]
# # for item in tuple10:
# #     print(item)
# #
# # #Множества
# #
# # #задание 1
# # set1 = {1,2,3,4,5,6}
# # print(set1)
# #
# # #задание 2
# # set2 = {1,2,3,4,5,6}
# # inputset = int(input("Введите число для проверки: "))
# # is_in_set = inputset in set2
# # print(is_in_set)
# #
# # #задание 3
# # set3 = {1,2,3,4,5,6}
# # set3.add(7)
# # print(set3)
# #
# # #задание 4
# # set4 = {1,2,3,4,5,6}
# # set4.remove(6)
# # print(set4)
# #
# # #задание 5
# # set5 = {1,2,3}
# # set6 = {4,5,6}
# # sumset = set5.union(set6)
# # print(sumset)
# #
# # #задание 6
# # set7 = {1,2,3,4}
# # set8 = {4,5,6,7}
# # interset = set7.intersection(set8)
# # print(interset)
# #
# # #задание 7
# # set9 = {1,2,3,4,5,6,7}
# # set10 = {4,5,6,7}
# # diffset = set9.difference(set10)
# # print(diffset)
# #
# # #задание 8
# # set11 = {1,2,3,4,5,6,7}
# # set12 = {4,5,6,7}
# # symset = set11.symmetric_difference(set12)
# # print(symset)
# #
# # #задание 9
# # set13 = {1,2,3,4,5,6,7}
# # set14 = {4,5,6,7}
# # print(set14.issubset(set13))
# #
# # #задание 10
# # set15 = {1,2,3,4,5,6,7}
# # for item in set15:
# #     print(item)
# #
# #Словари
#
# #задание 1
# student = {"имя": "илюша", "возраст": 15, "город": "краснодар"}
# print(student)
#
# #задание 2
# print(student["имя"], student["возраст"])
#
# #задание 3
# student["возраст"] = 16
# print(student)
#
# #задание 4
# student["хобби"] = "рисование"
# print(student)
#
# #задание 5
# student.pop("город")
# print(student)
#
# #задание 6
# inputstud = str(input("какая информация нужна: "))
# if inputstud in student:
#     print(True)
# else:
#     print(False)
#
# #задание 7
# for key in student:
#     print(key)
#
# for value in student.values():
#     print(value)
#
# #задание 8
# student2 = {"имя": "Давыд", "возраст": 18, "характер": "крутой мощный дерзкий жоский харизматичный"}
# student.update(student2)
# print(student)
#
# #задание 9
# inputstud2 = input("какой ключ нужен: ")
# if inputstud2 in student:
#     print(student.get(inputstud2))
# else:
#     print("такого ключа нет")
#
# #задание 10
# numbers = {1,2,3,4,5,6,7,8,9,10}
# sumnumbers=sum(numbers)
# print(sumnumbers)