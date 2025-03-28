import numpy as np
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def matrix_multiplication(A, B):
    return np.dot(A, B)

def recurrence_solver(T, n, func):
    if n == 1:
        return 1
    return func(T, n)

def recurrence1(T, n):
    return 2 * recurrence_solver(T, n // 4, recurrence1) + np.sqrt(n)

def recurrence2(T, n):
    return 2 * recurrence_solver(T, n // 4, recurrence2) + n

def recurrence3(T, n):
    return 16 * recurrence_solver(T, n // 4, recurrence3) + n**2

# Testing Recurrences
n_values = np.logspace(1, 4, num=20, dtype=int)
rec1_values = [recurrence_solver(None, n, recurrence1) for n in n_values]
rec2_values = [recurrence_solver(None, n, recurrence2) for n in n_values]
rec3_values = [recurrence_solver(None, n, recurrence3) for n in n_values]

plt.figure(figsize=(10, 5))
plt.plot(n_values, rec1_values, label='T(n) = 2T(n/4) + sqrt(n)')
plt.plot(n_values, rec2_values, label='T(n) = 2T(n/4) + n')
plt.plot(n_values, rec3_values, label='T(n) = 16T(n/4) + n^2')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.legend()
plt.title('Recurrence Relations Growth')
plt.show()
