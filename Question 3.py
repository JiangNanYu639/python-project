def sixes(fileName):
    f = open(fileName,'r')

    for line in f.readlines():
        line = line.strip()
        if not line.startswith('+'):
            if not line.startswith('-'):
                print(line,end = '')
                pass
            else:
                line = line.split(' ')
                cnt1 = 0
                cnt2 = 0
                str = line[0]
                while (cnt1 < len(str)):
                    if str[cnt1] == '+':
                        cnt2 += 1
                    cnt1 += 1
                ret = cnt2 / len(str) * 100
                print(': %.1f%% sixes'%(ret))
        else:
            line = line.split(' ')
            str = line[0]
            cnt1 = 0
            cnt2 = 0
            while (cnt1 < len(str)):
                if str[cnt1] == '+':
                    cnt2 += 1
                cnt1 += 1
            ret = cnt2 / len(str) * 100
            print(': %.1f%% sixes'%(ret))

    f.close()

sixes("input.txt")




