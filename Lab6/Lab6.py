from prettytable import PrettyTable

# One sided
# Правая разносторонняя производная
def right(y_cur, y_next, step):
    return (y_next - y_cur) / step

# Левая разносторонняя производная
def left(y_cur, y_prev, step):
    return (y_cur - y_prev) / step

def RightOneSided(ydata, step):
    result = []
    for i in range(len(ydata) - 1):
        result.append("{:.3f}".format(right(ydata[i], ydata[i + 1], step)))
    result.append("-")
    return result

def LeftOneSided(ydata, step):
    result = ["-"]
    for i in range(1, len(ydata)):
        result.append("{:.3f}".format(left(ydata[i], ydata[i - 1], step)))
    return result


# Central
# Центральная формула для левой производной
def center(y_next, y_prev, step):
    return (y_next - y_prev) / (2 * step)

# Центральная формула для x0
def center_x0(y_0, y_1, y_2, step):
    return (-3 * y_0 + 4 * y_1 - y_2) / (2 * step)

# для xn
def center_xn(y_n, yn_1, yn_2, step):
    return (3 * y_n - 4 * yn_1 + yn_2) / (2 * step)

def Central(input_data, step):
    result = [center_x0(input_data[0], input_data[1], input_data[2], step)]
    length = len(input_data)
    for i in range(1, length - 1):
        result.append(center(input_data[i + 1], input_data[i - 1], step))
    result.append(center_xn(input_data[length - 1], input_data[length - 2], input_data[length - 3], step))
    return ["{:.3f}".format(i) for i in result]


#Runge
# Вторая формула Рунге, в основе лежит правосторонняя формула
def runge_right(y_cur, y_next, y_next_next, step):
    return (4 * y_next - 3 * y_cur - y_next_next) / (2 * step)

# Вторая формула Рунге, в основе лежит левосторонняя формула
def runge_left(y_cur, y_prev, y_prev_prev, step):
    return (3 * y_cur - 4 * y_prev + y_prev_prev) / (2 * step)

def RightRunge(ydata, step):
    result = []
    for i in range(len(ydata) - 2):
        result.append("{:.3f}".format(runge_right(ydata[i], ydata[i + 1], ydata[i + 2], step)))
    result.append("-")
    result.append("-")
    return result

def LeftRunge(ydata, step):
    result = ["-", "-"]
    for i in range(2, len(ydata)):
        result.append("{:.3f}".format(runge_left(ydata[i], ydata[i - 1], ydata[i - 2], step)))
    return result


#Reshape
def eta(y):
    return 1 / y

def ksi(x):
    return 1 / x

# В основе лежит правосторонняя формула
def right_reshape(y_cur, y_next, x_cur, x_next):
    return (eta(y_next) - eta(y_cur)) / (ksi(x_next) - ksi(x_cur)) * (y_cur / x_cur) ** 2

# В основе лежит левосторонняя формула.
def left_reshape(y_cur, y_prev, x_cur, x_prev):
    return (eta(y_cur) - eta(y_prev)) / (ksi(x_cur) - ksi(x_prev)) * (y_cur / x_cur) ** 2

def RightReshape(xdata, ydata):
    result = []
    for i in range(len(ydata) - 1):
        result.append("{:.3f}".format(right_reshape(ydata[i], ydata[i + 1], xdata[i], xdata[i + 1])))
    result.append("-")
    return result

def LeftReshape(xdata, ydata):
    result = ["-"]
    for i in range(1, len(ydata)):
        result.append("{:.3f}".format(left_reshape(ydata[i], ydata[i - 1], xdata[i], xdata[i - 1])))
    return result


#Second central
def second_central(y_cur, y_prev, y_next, step):
    return (y_prev - 2 * y_cur + y_next) / step ** 2

def second_central_x0(y0, y1, y2, y3, step):
    return (4 * y2 - 5 * y1 - y3 + 2 * y0) / step ** 2

def second_central_xn(yn, yn_1, yn_2, yn_3, step):
    return (4 * yn_2 - 5 * yn_1 - yn_3 + 2 * yn) / step ** 2

def SecondCentral(ydata, step):
    result = ["{:.3f}".format(second_central_x0(ydata[0], ydata[1], ydata[2], ydata[3], step))]
    for i in range(1, len(ydata) - 1):
        result.append("{:.3f}".format(second_central(ydata[i], ydata[i - 1], ydata[i + 1], step)))
    n = len(ydata) - 1
    result.append("{:.3f}".format(second_central_xn(ydata[n], ydata[n - 1], ydata[n - 2], ydata[n - 3], step)))
    return result


#Main
def main():
    xdata = [1, 2, 3, 4, 5, 6]
    ydata = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

    table = [xdata, ydata, [], [], [], [], []]

    step = 1

    data_12 = RightOneSided(ydata, step)
    data_11 = LeftOneSided(ydata, step)
    data_2 = Central(ydata, step)
    data_32 = RightRunge(ydata, step)
    data_31 = LeftRunge(ydata, step)
    data_42 = RightReshape(xdata, ydata)
    data_41 = LeftReshape(xdata, ydata)
    data_5 = SecondCentral(ydata, step)

    table = PrettyTable()
    table.add_column("x", xdata)
    table.add_column("y", ydata)
    table.add_column("Левосторонняя", data_11)
    table.add_column("Правосторонняя", data_12)
    table.add_column("Центральная", data_2)
    table.add_column("Рунже, в основе л-я ф-ла", data_31)
    table.add_column("Рунже, в основе п-я ф-ла", data_32)
    table.add_column("Выравнивающая, в основе л-я ф-ла", data_41)
    table.add_column("Выравнивающая, в основе п-я ф-ла", data_42)
    table.add_column("Вторая центральная", data_5)

    print(table)

if __name__ == '__main__':
    main()
