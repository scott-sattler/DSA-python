import time

"""
conclusions:
performance (very large integers > multiple large integers > strings)

"""


def fn0(n):
    for i in range(n):
        if 12345 == 12345 + i:
            i = i + 1


def fn1(n):
    for i in range(n):
        if 1234567890 == 12345678 + i:
            i = i + 1


def fn2(n):
    for i in range(n):
        if 123456789012345678901234567890 == 12345678123456781234567800 + i:
            i = i + 1


def fn3(n):
    for i in range(n):
        #  0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000  100 digits  # noqa
        if (123456789012345678901234567890123456789012345678901234567890 ==
            1234567812345678123456780012345678123456781234567800 + i):  # noqa
            i = i + 1


def fn4(n):
    for i in range(n):
        #  0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000  100 digits  # noqa
        if (1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890 ==
            1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890 + i):  # noqa
            i = i + 1


def fn5(n):
    for i in range(n):
        if 123456789012345678901234567890 == (123456789012345678901234567890 + i):
            i = i + 1
        if 123456789012345678901234567890 == (123456789012345678901234567890 + i):
            i = i + 1
        if 123456789012345678901234567890 == (123456789012345678901234567890 + i):
            i = i + 1


def fn6(n):
    for i in range(n):
        each = [
            '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891',
            '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567892',
            '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567893'
        ]
        if ('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890' ==
            '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'):  # noqa
            i = i + 1


def fn7(n):
    for i in range(n):
        if 123456789012345678901234567890 == (123456789012345678901234567890 + i):
            i = i + 1
            if 123456789012345678901234567890 == (123456789012345678901234567890 + i):
                i = i + 1
                if 123456789012345678901234567890 == (123456789012345678901234567890 + i):
                    i = i + 1


loops = 100_000_000

# # fn 0-4, digit scaling
# start = time.perf_counter()
# fn1(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# start = time.perf_counter()
# fn2(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# start = time.perf_counter()
# fn3(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# start = time.perf_counter()
# fn3(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)


# # fn4 (100 digit int) vs fn5 (3 30 digit ints)
# print('\n4')
# start = time.perf_counter()
# fn4(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# print('\n5')
# start = time.perf_counter()
# fn5(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# print('\n5')
# start = time.perf_counter()
# fn5(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# print('\n4')
# start = time.perf_counter()
# fn4(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)


# # fn4 (100 digit int) vs fn6 (100 digit string)
# print('\n4')
# start = time.perf_counter()
# fn4(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# print('\n6')
# start = time.perf_counter()
# fn6(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# print('\n6')
# start = time.perf_counter()
# fn6(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)
#
# print('\n4')
# start = time.perf_counter()
# fn4(loops)
# stop = time.perf_counter()
# print(stop - start, start, stop)
# time.sleep(1)


# fn4 (100 digit int) vs fn7 (3 conditional 30 digit ints)
print('\n4')
start = time.perf_counter()
fn4(loops)
stop = time.perf_counter()
print(stop - start, start, stop)
time.sleep(1)

print('\n7')
start = time.perf_counter()
fn7(loops)
stop = time.perf_counter()
print(stop - start, start, stop)
time.sleep(1)

print('\n7')
start = time.perf_counter()
fn7(loops)
stop = time.perf_counter()
print(stop - start, start, stop)
time.sleep(1)

print('\n4')
start = time.perf_counter()
fn4(loops)
stop = time.perf_counter()
print(stop - start, start, stop)
time.sleep(1)
