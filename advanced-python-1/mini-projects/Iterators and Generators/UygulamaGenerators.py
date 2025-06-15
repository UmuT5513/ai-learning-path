def square(n=0):
    while True:
        yield n*n
        n+=1

generator = square()

for i in range(10):
    print(next(generator))  # 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

# This code demonstrates the use of a generator to yield square numbers


def fibonacci(max):
    a, b=0,1
    count=0
    while count < max:
        yield a
        a = b
        b = a+b
        count+=1

# generator = fibonacci(9000)
# for i in generator:
#     print(i)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


import sys
list = [i for i in range(10000)]
gen_list = (i for i in range(10000))
print(sys.getsizeof(list))  # 80000
print(sys.getsizeof(gen_list))  # 104

import time

list_start_time = time.time()
sum([i for i in range(1000000)])
list_end_time = time.time() - list_start_time

gen_start_time = time.time()
sum((i for i in range(1000000)))
gen_end_time = time.time() - gen_start_time

print(f"List time: {list_end_time} seconds")
print(f"Generator time: {gen_end_time} seconds")

# This code demonstrates the use of a generator to yield Fibonacci numbers
# and compares the memory usage and performance of a list versus a generator.