#include <iostream>

using namespace std;

double *get_difs(int x, int n, int size, const double table[][3])
{
    double difs[n];

    double new_table[n][2];
    new_table[0][0] = table[0][0];
    new_table[0][1] = table[0][1];

    int id = 0;

    for (int i = 0; i < size; i++)
    {
        if (x > table[i][0])
        {
            new_table[0][0] = table[i][0];
            new_table[0][1] = table[i][1];
            id = i;
        }
    }

    return difs;
}

int main()
{
    //                            X        Y         Y'
    const double table[8][3] = {{0.00, 1.000000, -1.00000},
                                {0.15, 0.838771, -1.14944},
                                {0.30, 0.655336, -1.29552},
                                {0.45, 0.450447, -1.43497},
                                {0.60, 0.225336, -1.56464},
                                {0.75,-0.018310, -1.68164},
                                {0.90,-0.278390, -1.78333},
                                {1.05,-0.552430, -1.86742}};

    const double table2[5][3]= {{0.00, 1.0,   1},
                                {0.25, 0.924, 2},
                                {0.50, 0.707, 3},
                                {0.75, 0.383, 4},
                                {1.0, 0.0,    5}};



    return 0;
}
