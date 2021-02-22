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
    rez.append(table2[0])
    index = 0;
    for i in range(len(table2)):
        if table2[i][0] <= x:
            rez[0] = table2[i]
            index = i

    tmp = 1
    for i in range(0, n - 1):
        if (i % 2 == 0):
            rez.append(table2[index + tmp])
        else:
            rez.insert(0, table2[index - tmp])
            tmp += 1
    return rez

def get_dif(data, yi, yj, xi, xj):
    dif = (data[yi][1] - data[yj][1]) / (data[xi][0] - data[xj][0])
    return dif

def calculate_difs(data, n):
    rez = list(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            rez[j + i][1] = get_dif(rez, j, j + 1, j, j + 1 + i)
    return rez

number = 5

new_data = make_data(0.5, number)

print(new_data)

new_difs = calculate_difs(new_data, number)

print(new_difs)

