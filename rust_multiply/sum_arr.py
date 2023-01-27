import rust 
import timeit 

rust_sm = lambda : rust.sum([i for i in range(100)])
t1 = timeit.timeit(rust_sm, number=1_000)
t2 = timeit.timeit(lambda : sum([i for i in range(100)]), number=1_000)
print(t1)
print(t2)

print('--10k')
rust_sm = lambda : rust.sum([i for i in range(1_0_000)])
t1 = timeit.timeit(rust_sm, number=100)
t2 = timeit.timeit(lambda : sum([i for i in range(1_0_000)]), number=100)
print(t1)
print(t2)

print('--100k')
rust_sm = lambda : rust.sum([i for i in range(1_00_000)])
t1 = timeit.timeit(rust_sm, number=10)
t2 = timeit.timeit(lambda : sum([i for i in range(1_00_000)]), number=10)
print(t1)
print(t2)

print('--1M')
rust_sm = lambda : rust.sum([i for i in range(1_000_000)])
t1 = timeit.timeit(rust_sm, number=1)
t2 = timeit.timeit(lambda : sum([i for i in range(1_000_000)]), number=1)
print(t1)
print(t2)
