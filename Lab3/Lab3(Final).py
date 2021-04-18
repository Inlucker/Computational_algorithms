#Newton Interpolation
from math import fabs, ceil

# Search for the beginning of the polynomial
def find_beginning(x, table, table_size, nearest_value, degree):

    degree += 1

    # Point to the left of segment:
    if (nearest_value == 0 and table[nearest_value] > x):
        print('Error!')
        return 0

    # Point to the right of segment:
    if (nearest_value == table_size - 1 and table[nearest_value] < x):
        print('Error!')
        return table_size - degree - 1

    # Point to the left of the nearby or equal of the nearby:
    if (x <= table[nearest_value]):
        if (nearest_value < (degree) / 2):
            return 0

        if ((table_size - 1 - nearest_value) < (ceil(degree / 2) - 1)):
            return table_size - degree - 1

        return nearest_value - degree / 2

    # Point to the right of the nearby:
    if (x > table[nearest_value]):
        if (nearest_value < (ceil(degree / 2) - 1)):
            return 0

        if (table_size - 1 - degree < degree / 2):
            return table_size - 1 - degree

        return nearest_value - (ceil(degree / 2) - 1)

    return 0

# Search for the nearest value y0
def nearest_value(x, table, size_table):

    if (x < table[0]):
        return 0

    if (x > table[size_table - 1]):
        return size_table - 1

    difference = fabs(x - table[0])
    for_first_y = 0

    for index in range(1, size_table):
        if (fabs(x - table[index]) < difference):
            for_first_y = index
            difference = fabs(x - table[index])

    return for_first_y

# Finding the value of Newton's interpolation polynomial:
def newton_polinom(x, degree, beginnig, table_x, table_y):

    result = table_y[beginnig]

    for i in range((beginnig + 1), beginnig + degree):
        divided = 0
        for j in range(beginnig, i + 1):
            difference = 1
            for k in range(beginnig, i + 1):
                if (k != j):
                    difference *= (table_x[j] - table_x[k])
            divided += (table_y[j] / difference)
        for k in range(beginnig, i):
            divided *= (x - table_x[k])
        result += divided

    return result

def newton_interpolation(x, x_table, y_table, degree):
    for_first_y = nearest_value(x, x_table, len(x_table))
    beginning = find_beginning(x, x_table, len(x_table), for_first_y, degree)
    return newton_polinom(x, degree, int(beginning), x_table, y_table)


#Spline Interpolation
def build_spline(x, y, n):
    # Инициализация массива сплайнов
    #          [a, b, c, d, x]
    splines = [[0, 0, 0, 0, 0] for _ in range(0, n)]
    for i in range(0, n):
        splines[i][4] = x[i]
        splines[i][0] = y[i]

    splines[0][2] = splines[n - 1][2] = 0.0

    # Решение СЛАУ относительно коэффициентов сплайнов c[i] методом прогонки для трехдиагональных матриц
    # Вычисление прогоночных коэффициентов - прямой ход метода прогонки
    alpha = [0.0 for _ in range(0, n - 1)]
    beta = [0.0 for _ in range(0, n - 1)]

    for i in range(1, n - 1):
        hi = x[i] - x[i - 1]
        hi1 = x[i + 1] - x[i]
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z

    # Нахождение решения - обратный ход метода прогонки
    for i in range(n - 2, 0, -1):
        splines[i][2] = alpha[i] * splines[i + 1][2] + beta[i]

    # По известным коэффициентам c[i] находим значения b[i] и d[i]
    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        splines[i][3] = (splines[i][2] - splines[i - 1][2]) / hi
        splines[i][1] = hi * (2.0 * splines[i][2] + splines[i - 1][2]) / 6.0 + (y[i] - y[i - 1]) / hi
    #print(splines)
    return splines

# Вычисление значения интерполированной функции в произвольной точке
def spline_interpolation(splines, x):
    n = len(splines)
    #   [a, b, c, d, x]
    s = [0, 0, 0, 0, 0]

    if x <= splines[0][4]:  # Если x меньше точки сетки x[0] - пользуемся первым эл-тов массива
        s = splines[0]
    elif x >= splines[n - 1][4]:  # Если x больше точки сетки x[n - 1] - пользуемся последним эл-том массива
        s = splines[n - 1]
    else:  # Иначе x лежит между граничными точками сетки - производим бинарный поиск нужного эл-та массива
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            # if x <= splines[k].x:
            if x <= splines[k][4]:
                j = k
            else:
                i = k
        s = splines[j]

    # dx = x - s.x
    dx = x - s[4]
    #print(s)
    # Вычисляем значение сплайна в заданной точке по схеме Горнера
    return s[0] + (s[1] + (s[2] / 2.0 + s[3] * dx / 6.0) * dx) * dx;


#Main Program
def function(x):
    y = x**2
    return y

def main():
    x_table = []
    y_table = []
    for i in range(11):
        x_table.append(i)
        y_table.append(function(i))

    #x = float(input("Введите x: "))
    for x in range(0, 101):
        x = x/10
        spline = build_spline(x_table, y_table, len(y_table))
        print("Введите x:", x)
        print("Реальное значение = {:^7f}".format(function(x)))
        print("Интерполяция сплайнами = {:^7f}".format(spline_interpolation(spline, x)))
        print("Интерполяция полиномом Ньютона (3-ей степени) = {:^7f}".format(newton_interpolation(x, x_table, y_table, 3)))
        print()

if __name__ == '__main__':
    main()