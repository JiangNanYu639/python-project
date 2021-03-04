# TA2 设计课程选择管理器，支持课程的增加，删除，修改，查询

myCourses = []

while True:
    print('Welcome to my system!\nPls input your choice:\n1.add a course\n2.remove a course\n3.search for a course\n4.exit\n')
    num = input('Pls input your choice: ')

    if not num.isdigit() or not (int(num)>0 and int(num)<5):
        print('Error input.')
    else:
        num = int(num)
        if num == 1:
            add = input('Pls input a course name: ')
            myCourses.append(add)
        elif num == 2:
            rem = input('Pls input a course name: ')
            if rem in myCourses:
                myCourses.remove(rem)
            else:
                print('Not an existed course.')
        elif num == 3:
            search = input('Pls input a course name: ')
            if search in myCourses:
                print('Found!')
            else:
                print('Not found.')
        else:
            print('See you again.')
            break

        print(myCourses)



