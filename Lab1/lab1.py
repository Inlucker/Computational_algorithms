table1 = [(0.00, 1.000000, -1.00000),
          (0.15, 0.838771, -1.14944),
          (0.30, 0.655336, -1.29552),
          (0.45, 0.450447, -1.43497),
          (0.60, 0.225336, -1.56464),
          (0.75,-0.018310, -1.68164),
          (0.90,-0.278390, -1.78333),
          (1.05,-0.552430, -1.86742)]

'''
table3 = ((0.00, 1.000000, -1.00000),
          (0.15, 0.838771, -1.14944),
          (0.30, 0.655336, -1.29552),
          (0.45, 0.450447, -1.43497),
          (0.60, 0.225336, -1.56464),
          (0.75,-0.018310, -1.68164),
          (0.90,-0.278390, -1.78333),
          (1.05,-0.552430, -1.86742))
'''

'''
table2 = ([0.00, 1.0,   1],
          [0.25, 0.924, 2],
          [0.50, 0.707, 3],
          [0.75, 0.383, 4],
          [1.0, 0.0,    5])
'''

#print (table)

def make_data_Newton(x, n, table):
    n += 1
    rez = []
    rez.append(list(table[len(table) - 1]))
    index = len(table) - 1
    '''
    for i in range(len(table)):
        if table[i][0] <= x:
            rez[0] = list(table[i])
            index = i
    '''
    for i in range(1, len(table)):
        if (x - table[i - 1][0]) * (x - table[i][0]) < 0:
            rez[0] = list(table[i - 1])
            index = i - 1
    #print(rez[0])
    #'''

    tmp = 1
    #print(rez)

    for i in range(0, n - 1):
        if (i % 2 == 0):
            if (index + tmp < len(table)):
                rez.append(list(table[index + tmp]))
            elif (index - tmp >= 0):
                rez.append(list(table[index - tmp]))
                tmp += 1
            else:
                print("Not enough data")
                rez = []
                break
        else:
            if (index - tmp >= 0):
                rez.append(list(table[index - tmp]))
                tmp += 1
            elif (index + tmp + 1 < len(table)):
                tmp += 1
                rez.append(list(table[index + tmp]))
                tmp += 1
            else:
                print("Not enough data")
                rez = []
                break

    #print(rez)
    return rez

def make_data_Ermit(x, n, table):
    n += 1
    rez = []
    rez.append(list(table[len(table) - 1]))
    index = len(table) - 1
    for i in range(1, len(table)):
        if (x - table[i - 1][0]) * (x - table[i][0]) < 0:
            rez[0] = list(table[i - 1])
            index = i - 1

    tmp = 1
    #print(rez)

    counter = 1
    down = 1

    while (counter < n):
        #print (rez)
        if (counter % 2 == 1):
            rez.append(list(rez[counter - 1]))
        else:
            if (down):
                if (index + tmp < len(table)):
                    rez.append(list(table[index + tmp]))
                elif (index - tmp >= 0):
                    rez.append(list(table[index - tmp]))
                    tmp += 1
                else:
                    print("Not enough data")
                    rez = []
                    break
            else:
                if (index - tmp >= 0):
                    rez.append(list(table[index - tmp]))
                    tmp += 1
                elif (index + tmp + 1 < len(table)):
                    tmp += 1
                    rez.append(list(table[index + tmp]))
                    tmp += 1
                else:
                    print("Not enough data")
                    rez = []
                    break
            down = (down + 1) % 2
        counter += 1

    return rez


def get_dif(data, yi, yj, xi, xj):
    if (data[xi][0] == data[xj][0]):
        dif = data[xi][2]
    else:
        dif = (data[yi][1] - data[yj][1]) / (data[xi][0] - data[xj][0])
    return dif

def calculate_polinom(data, n, x):
    n += 1
    rez = data[0][1]
    difs = list(data)
    #print(difs)
    #print(rez)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            difs[j][1] = get_dif(difs, j, j + 1, j, j + 1 + i)
        tmp = difs[0][1]
        for k in range (i + 1):
            tmp *= x - difs[k][0]
        rez += tmp
        #print("Difs = ", difs)
        #print("Rez = ", rez)
        #print("Tmp = ", tmp)

    return rez

'''
def calculate_polinom_Ermit(data, n, x):
    rez = data[0][1]
    difs = list(data)
    #print(difs)
    #print(rez)
    for i in range(n):
        for j in range(n - i):
            difs[j][1] = get_dif(difs, j, j + 1, j, j + 1 + i)
        tmp = difs[0][1]
        for k in range (i + 1):
            #mn = x - difs[k][0]
            tmp *= x - difs[k][0]
        rez += tmp
        #print("Difs = ", difs)
        #print("Rez = ", rez)
        #print("Tmp = ", tmp)

    return rez
'''

#cur_x = 0.525
#cur_x = 1.05
cur_x = float(input("Введите x: "))
print("x =", cur_x)

print ("|-------------------------------|")
print ("| Степень |  Ньютон  |  Эрмит   |")
print ("|-------------------------------|")
for i in range(1, 5):
    stepen = i
    #print("Степень =", stepen)
    print("|{:^9d}".format(stepen), end = "")

    new_data_Newton = make_data_Newton(cur_x, stepen, table1)

    #print(new_data_Newton)

    if (not new_data_Newton == []):
        polinom_Newton = calculate_polinom(new_data_Newton, stepen, cur_x)
        if (polinom_Newton > 0):
            print("| {:^8.6f} |".format(polinom_Newton), end = "")
        else:
            print("|{:^8.6f} |".format(polinom_Newton), end = "")

    new_data_Ermit = make_data_Ermit(cur_x, stepen, table1)
    #print(new_data_Ermit)

    if (not new_data_Ermit == []):
        polinom_Ermit = calculate_polinom(new_data_Ermit, stepen, cur_x)
        if (polinom_Ermit > 0):
            print(" {:^8.6f} |".format(polinom_Ermit), end = "")
        else:
            print("{:^8.6f} |".format(polinom_Newton), end = "")

    print("\n|-------------------------------|")

cur_y = 0

inverse_table1 = []
for i in range(len(table1)):
    #inverse_table1.insert(0, (table1[i][1], table1[i][0]))
    inverse_table1.append((table1[i][1], table1[i][0]))
#print(inverse_table1)

print ("|--------------------|")
print ("| Степень |  Корень  |")
print ("|--------------------|")
for i in range(1, 5):
    stepen = i
    #print("Степень =", stepen)
    print("|{:^9d}".format(stepen), end = "")

    new_data_Newton = make_data_Newton(cur_y, stepen, inverse_table1)

    #print(new_data_Newton)

    if (not new_data_Newton == []):
        polinom_Newton = calculate_polinom(new_data_Newton, stepen, cur_y)
        if (polinom_Newton > 0):
            print("| {:^8.6f} |".format(polinom_Newton), end = "")
        else:
            print("|{:^8.6f} |".format(polinom_Newton), end = "")

    print("\n|--------------------|")