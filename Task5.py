#student_of_fist = int(input('Enter num of student of fist class: '))
#student_of_second = int(input('Enter num of student of second class:'))
#student_of_third = int(input('Enter num of student of third class: '))

#result=(student_of_fist+student_of_second+student_of_third)/2

#print('Result= ', result)


students1 = int(input('Количество студентов в 1ом классе: '))
students2 = int(input('Количество студентов во 2ом классе: '))
students3 = int(input('Количество студентов в 3ем классе: '))

tab_class1 = students1 // 2
ost1 = students1 % 2
if ost1 > 0:
tab_class1 += 1

tab_class2 = students2 // 2
ost2 = students2 % 2
if ost2 > 0:
tab_class2 += 1

tab_class3 = students3 // 2
ost3 = students3 % 2
if ost3 > 0:
tab_class3 += 1

all_tables = tab_class1 + tab_class2 + tab_class3

message = int(all_tables)

print('Всего надо: %s столов' %message)
