z_table = [ (0, 1, 4, 9, 16),
            (1, 2, 5, 10, 17),
            (4, 5, 8, 13, 20),
            (9, 10, 13, 18, 25),
            (16, 17, 20, 25, 32) ]

def get_xy_array(x, stepen):
    min_el = 0
    min_id = 0
    for i in range (1, 4):
        if abs(x - i) < x - min_el:
            min_el = i
            min_id = i
    rez = [min_el]

    #x_array = [0, 1, 2, 3, 4]
    cur_id = min_id
    for i in range(stepen):
        if (i % 2 == 0):
            cur_id = max(rez) + 1
        else:
            cur_id = min(rez) - 1

        if (cur_id > 4):
            cur_id = min(rez) - 1

        if (cur_id < 0):
            cur_id = max(rez) + 1

        if (cur_id <= 4 and cur_id >= 0):
            rez.append(cur_id)
        else:
            print("get_x_array ERROR!")

    rez.sort()
    return rez

def get_diff(y, *args):
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return y[args[0]]
    else:
        return (get_diff(y, *args[:-1]) - get_diff(y, *args[1:])) / (args[0] - args[-1])


def get_polinom(xi, y):
    polinom = []
    for i in range(len(xi)):
        k = xi[:i]
        polinom.append(k)
        diff = get_diff(y, *xi[:(i + 1)])
        polinom.append(diff)
    return polinom


def take_x(brackets, x):
    if not brackets:
        return 1
    result = 1
    for bracket in brackets:
        result *= (x - bracket)
    return result


def calc_value(polinom, x):
    result = 0
    for i in range(0, len(polinom), 2):
        result += take_x(polinom[i], x) * polinom[i + 1]
    return result


def mult_interpol(x, y, stepen_x, stepen_y):
    x_array = get_xy_array(x, stepen_x)
    y_array = get_xy_array(y, stepen_y)
    xi_values = dict()
    for i in y_array:
        polinom = get_polinom(x_array, z_table[i])
        xi_values[i] = calc_value(polinom, x)

    polinom = get_polinom(y_array, xi_values)
    z = calc_value(polinom, y)
    print("|{:^7d}|{:^7d}".format(stepen_x, stepen_y), end = "")
    print("| {:^12.6f} |".format(z), end = "")
    print("\n|------------------------------|")


def main():
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))

    print("|------------------------------|")
    print("| Степени Nx,Ny |    Z(X,Y)    |")
    print("|------------------------------|")
    for i in range(1, 4):
        #for j in range(1, 4):
        mult_interpol(x, y, i, i)

if __name__ == '__main__':
    main()