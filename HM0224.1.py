# 输入一个成绩，如: 67分，得到'C'成绩
# 85-100 'A'
# 75-84  'B'
# 60-74  'C'
# 0-59   'D'

grade = input('pls input your grade: ')
grade = float(grade)

if (grade > 84 and grade <= 100):
    print('You got an A.')
elif (grade > 74 and grade <= 84):
    print('You got a B.')
elif (grade > 59 and grade <= 74):
    print('You got a C.')
elif (grade >= 0 and grade <= 59):
    print('You got a D.')
else:
    print('Not a valid grade.')