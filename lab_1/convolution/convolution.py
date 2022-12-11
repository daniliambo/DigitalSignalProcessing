import numpy as np

signal = [1, 2, 3, 4, 5]
kernel = [10, 7, 5, 3]

# sof implementation
def convolve(signal, kernel):
    kernel = kernel[::-1]
    return [
        np.dot(
            signal[max(0, i):min(i + len(kernel), len(signal))],
            kernel[max(-i, 0):len(signal) - i * (len(signal) - len(kernel) < i)], )
        for i in range(1 - len(kernel), len(signal))
    ]
print(convolve(signal, kernel))

# Nurlan's implementation
# def convolve(in1, in2):
#     res = [0] * (len(in1) + len(in2) - 1)
#     for i in range(len(res)):
#         if i >= len(in2):
#             k = i - len(in2) + 1
#         else:
#             k = 0
#         sum = 0
#         while True:
#             if 0 <= i - k < len(in2) and 0 <= k < len(in1):
#                 sum += in1[k] * in2[i - k]
#                 k += 1
#             else:
#                 res[i] = sum
#                 break
#     return res
