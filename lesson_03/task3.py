import math, random
import numpy as np


print("\nЗадача 1. Инвентаризация массива.\n")

m = np.arange(60).reshape(3, 4, 5)

print(f"shape - {m.shape}")
print(f"ndim - {m.ndim}")
print(f"size - {m.size}")
print(f"dtype - {m.dtype}")
print(f"strides - {m.strides}")
print(f"C_CONTIGUOUS - {m.flags['C_CONTIGUOUS']}")


print("\nЗадача 2. int vs float — тихая ловушка.\n")

a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3], dtype=np.int8)

print(f"a / 2 - {a / 2}")
print(f"a // 2 - {a // 2}")
print(f"a / 2.0 - {a / 2.0}")
print(f"a.dtype - {a.dtype}")
print(f"(a / 2).dtype - {(a / 2).dtype}")
print(f"(a // 2).dtype - {(a // 2).dtype}")

print(f"b + 127 - {b + 127}")
print(f"b.dtype - {b.dtype}")


print("\nЗадача 3. float32 vs float64 — реальная точность.\n")

numb_a = float(np.float32(0.1)) - 0.1
numb_b = float(np.float64(0.1)) - 0.1

print(f"a - {numb_a:.20e}")
print(f"b - {numb_b:.20e}")


print("\nЗадача 4. Явный dtype при создании.\n")

arr1_64 = np.zeros((2, 3), dtype=np.float64)
arr2_32 = np.zeros((2, 3), dtype=np.float32)
arr3_16 = np.ones((2, 3), dtype=np.int16)
arr4_8 = np.full((2, 3), 7, dtype=np.uint8)

print(f"float64 dtype - {arr1_64.dtype}")
print(f"float64 nbytes - {arr1_64.nbytes}")
print(f"float32 dtype - {arr2_32.dtype}")
print(f"float32 nbytes - {arr2_32.nbytes}")
print(f"int16 dtype - {arr3_16.dtype}")
print(f"int16 nbytes - {arr3_16.nbytes}")
print(f"uint8 dtype - {arr4_8.dtype}")
print(f"uint8 nbytes - {arr4_8.nbytes}")

arr1_64_1000 = np.zeros((1000, 1000), dtype=np.float64)
arr2_32_1000 = np.zeros((1000, 1000), dtype=np.float32)

print(f"float64 1000 x 1000 nbytes - {arr1_64_1000.nbytes}")
print(f"float32 1000 x 1000 nbytes - {arr2_32_1000.nbytes}")


print("\nЗадача 5. Цепочка reshape.\n")

a = np.arange(24)
print(f"a shape - {a.shape}")
print(f"a shape (4 - 6) - {a.reshape(4, 6).shape}")
print(f"a (4 - 6) == a - {np.array_equal(a, a.reshape(4, 6).ravel())}")
print(f"a shape (2 - 3 - 4) - {a.reshape(2, 3, 4).shape}")
print(f"a (2 - 3 - 4) == a - {np.array_equal(a, a.reshape(2, 3, 4).ravel())}")
print(f"a shape (2 - 2 - 6) - {a.reshape(2, 2, 6).shape}")
print(f"a (2 - 2 - 6) == a - {np.array_equal(a, a.reshape(2, 2, 6).ravel())}")
print(f"a shape (24) - {a.reshape(24).shape}")
print(f"a (24) == a - {a.reshape(24).shape}")


print("\nЗадача 6. flatten vs ravel — копия или view.\n")

M = np.arange(12).reshape(3, 4)

f = M.flatten() 
r = M.ravel()

print("\nf.base is None:", f.base is None)
print("r.base is not None:", r.base is not None)
print("r.base is M:", r.base is M)
print("np.shares_memory(M, f):", np.shares_memory(M, f))  
print("np.shares_memory(M, r):", np.shares_memory(M, r))  

f[0] = 999
r[1] = 888
print("\nf[0] = 999: M[0,0] =", M[0, 0]) 
print("r[1] = 888: M[0,1] =", M[0, 1]) 


print("\nЗадача 7. newaxis, squeeze, транспонирование.\n")

v = np.arange(5)

print(f"1: {v[:, None].shape}")
print(f"2: {v[None, :].shape}")
print(f"3: {np.squeeze(v[:, None]).shape}")
print(f"4: {np.arange(6).reshape(2, 3).T.shape}")


print("\nЗадача 8. Транспонирование без копии.\n")

A = np.arange(6).reshape(2, 3)
B = A.T

print(f"B not none: {B.base is not None}")

B[0, 1] = 999
print(f"B[0, 1] = 999, A[1, 0]: {A[1, 0]}")


print("\nЗадача 9. Поэлементно vs матричное.\n")


A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)

print(f"A @ B = {A @ B}")
print(f"A @ B shape = {(A @ B).shape}")
# print(f"A.T * B.T = {A.T * B.T}")
# print(f"A.T * B.T shape = {(A.T * B.T).shape}")
print(f"A * A = {A * A}")
print(f"A * A shape = {(A * A).shape}")
# print(f"A * B = {A * B}")
# print(f"A * B shape = {(A * B).shape}")

 
print("\nЗадача 10. axis=0 vs axis=1.\n")

M = np.arange(12).reshape(3, 4)

print(M)

print("M.sum(axis=0) =", M.sum(axis=0))
print("M.sum(axis=1) =", M.sum(axis=1))
print("M.mean(axis=0) =", M.mean(axis=0))
print("M.mean(axis=1) =", M.mean(axis=1))
print("M.argmax(axis=0) =", M.argmax(axis=0))
print("M.argmax(axis=1) =", M.argmax(axis=1))


print("\nЗадача 11. keepdims и broadcasting.\n")

X = np.random.default_rng(42).normal(size=(5, 3))
print("X shape =", X.shape)
print("axis=0 =", X.mean(axis=0))
print("axis=0 keep =", X.mean(axis=0, keepdims=True))
print("X - X.axis=0 shape =", (X - X.mean(axis=0)).shape)
print("X - X.axis=0 keep shape =", (X - X.mean(axis=0, keepdims=True)).shape)
print("==", np.allclose((X - X.mean(axis=0)).shape, (X - X.mean(axis=0, keepdims=True)).shape))

print("std axis=1 =", X.std(axis=1).shape)
print("std axis=1 keep =", X.std(axis=1, keepdims=True).shape)

normStr = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
print("Z.shape =", normStr.shape)
print("normStd mean =", normStr.mean(axis=1))
print("normStd std =", normStr.std(axis=1))


print("\nЗадача 12. Срез — view, не копия.\n")

a = np.arange(10)
b = a[2:5]

print("a =", a)

b[0] = 999

print("b =", b)
print("a =", a)

a = np.arange(10)
c = a[2:5].copy()
c[0] = 999

print("a =", a)
print("c =", c)
print("a =", a)
