table = ([0.00, 1.000000, -1.00000],
         [0.15, 0.838771, -1.14944],
         [0.30, 0.655336, -1.29552],
         [0.45, 0.450447, -1.43497],
         [0.60, 0.225336, -1.56464],
         [0.75,-0.018310, -1.68164],
         [0.90,-0.278390, -1.78333],
         [1.05,-0.552430, -1.86742])

table2 = ([0.00, 1.0,   1],
          [0.25, 0.924, 2],
          [0.50, 0.707, 3],
          [0.75, 0.383, 4],
          [1.0, 0.0,    5])

#print (table)

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

def get_dif(data, yi, yj, xi, xj):
    dif = (data[yi][1] - data[yj][1]) / (data[xi][0] - data[xj][0])
    return dif

def calculate_polinom_Newton(data, n, x):
    rez = data[0][1]
    difs = list(data)
    #print(difs)
    #print(rez)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            difs[j][1] = get_dif(difs, j, j + 1, j, j + 1 + i)
        tmp = difs[0][1]
        for k in range (i + 1):
            mn = x - difs[k][0]
            tmp *= x - difs[k][0]
        rez += tmp
        #print("Difs = ", difs)
        #print("Rez = ", rez)
        #print("Tmp = ", tmp)

    return rez

number = 5

cur_x = 0.525

new_data = make_data(cur_x, number)

print(new_data)

polinom = calculate_polinom_Newton(new_data, number, cur_x)

print(polinom)

