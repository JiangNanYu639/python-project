# 平面范围内有三个点A、B、C: A(2.5,3.7) ,B(3,9) ,C(4,4.5) 计算一下哪两个点最近

Ax = 2.5
Bx = 3
Cx = 4

Ay = 3.7
By = 9
Cy = 4.5

AB = ((Bx-Ax)**2+(By-Ay)**2)**0.5
AC = ((Cx-Ax)**2+(Cy-Ay)**2)**0.5
BC = ((Cx-Bx)**2+(Cy-By)**2)**0.5

if AB < AC:
    if AB < BC:
        print('Min is AB.')
    elif AB > BC:
        print('Min is BC.')
    else:
        print('Mins are AB and BC.')
elif AB > AC:
    if AC > BC:
        print('Min is BC.')
    elif AC < BC:
        print('Min is AC.')
    else:
        print('Mins are AC and BC.')
else:
    if AB < BC:
        print('Mins are AB and AC.')
    elif AB > BC:
        print('Min is BC.')
    else:
        print('AB, AC and BC are equal.')


