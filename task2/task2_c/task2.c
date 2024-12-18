#include "task2.h"
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


double f(double const x, double const y) {
    return 0.;
}

EXPORT void TASK2_run(
    int const n_points,
    double const eps,
    double const
    temperature, double const std,
    int const threads,
    char path[]
) {
    omp_set_num_threads(threads);

    double const h = 1. / ((double)n_points - 1);
    double **F = (double**)calloc(n_points, sizeof(double*)),
           **U = (double**)calloc(n_points + 2, sizeof(double*));

    for (int i = 0; i < n_points; ++i) {
        F[i] = (double*)calloc(n_points, sizeof(double));
        U[i] = (double*)calloc(n_points + 2, sizeof(double));
    }

    U[n_points] = (double*)calloc(n_points + 2, sizeof(double));
    U[n_points + 1] = (double*)calloc(n_points + 2, sizeof(double));

    for (int i = 0; i < n_points; ++i) {
        for (int j = 0; j < n_points; ++j) {
            if (i == 0) {
                U[0][j + 1] = U[n_points + 1][j + 1] = temperature;
            }

            F[i][j] = f((double)i * h, (double)j * h);
            U[i + 1][j + 1] = ((double)rand() / RAND_MAX * 2 - 1) * std;
        }
        U[i][0] = U[i][n_points + 1] = temperature;
    }
    U[n_points][0] = U[n_points][n_points + 1] = U[n_points + 1][0] = U[n_points + 1][n_points + 1] = temperature;

    double dm = 0, d_max = 1;
    double const h2 = h * h;

    while (d_max > eps) {
        d_max = 0;

        int i, j;
        double temp;

#pragma omp parallel for collapse(2) reduction(max: d_max) default(none) shared(U, F, n_points, h2, eps)\
     private(i, j, temp, dm)
        for (i = 1; i < n_points + 1; ++i) {
            for (j = 1; j < n_points + 1; ++j) {
                temp = U[i][j];

                U[i][j] = 0.25 * (U[i - 1][j] + U[i + 1][j] + U[i][j - 1] + U[i][j + 1] - h2 * F[i - 1][j - 1]);

                dm = fabs(temp - U[i][j]);

                if (d_max < dm) {
                    d_max = dm;
                }
            }
        }
    }

    FILE *file = fopen(path, "w+");

    for (int i = 0; i < n_points; ++i) {
        for (int j = 0; j < n_points; ++j) {
            fprintf(file, "%e ", U[i + 1][j + 1]);
        }
        fprintf(file, "\n");
    }

    fclose(file);

    for (int i = 0; i < n_points; ++i) {
        free(F[i]);
        free(U[i]);
    }

    free(U[n_points]);
    free(U[n_points + 1]);

    free(F);
    free(U);
}
