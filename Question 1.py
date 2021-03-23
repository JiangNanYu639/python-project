def superset(m1, m2):
    if isinstance(m1, dict) and isinstance(m2, dict):
        for i, j in m1.items():
            if i not in m2:
                return False
            else:
                if j != m2[i]:
                    return False
        return True
    else:
        str = 'Inputs must be dicts.'
        return str

d1 = {7:1, 18:5, 42:3, 76:10, 98:2, 234:50}
d2 = {7:2, 11:9, 42:-12, 98:4, 234:0, 9999:3}
d3 = {7:1, 18:5, 42:3, 76:10, 98:2, 234:50}
d4 = {7:1, 18:5, 42:3, 76:10, 98:2, 234:50, 9999:3}
d5 = {}
d6 = 100

ret = superset(d1, d5)
print(ret)