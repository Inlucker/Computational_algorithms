table = [(0.00, 1.000000, -1.00000),
         (0.15, 0.838771, -1.14944),
         (0.30, 0.655336, -1.29552),
         (0.45, 0.450447, -1.43497),
         (0.60, 0.225336, -1.56464),
         (0.75,-0.018310, -1.68164),
         (0.90,-0.278390, -1.78333),
         (1.05,-0.552430, -1.86742)]

print (table)

def make_data(x, n):
    rez = []
    rez.append(table[0])
    index = 0;
    for i in range(len(table)):
        if table[i][0] <= x:
            rez[0] = table[i]
            index = i

    tmp = 1
    for i in range(0, n - 1):
        if (i % 2 == 0):
            rez.append(table[index + tmp])
        else:
            rez.insert(0, table[index - tmp])
            tmp += 1
    return rez

print(make_data(0.5, 4))
