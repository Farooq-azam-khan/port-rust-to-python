import timeit 
import rust 
rust_mult = lambda : rust.multiply(2,3)
t1 = timeit.timeit(rust_mult, number=1_000)
t2 = timeit.timeit(lambda : 2*3, number=1_000)
print(t1)
print(t2)
