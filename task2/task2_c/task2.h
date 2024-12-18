#ifndef TASK2_H
#define TASK2_H

#if defined(_WIN32) || defined(_WIN64)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

EXPORT void TASK2_run(int n_points, double eps, double temperature, double std, int threads, char path[]);

#endif
