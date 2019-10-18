#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://projecteuler.info/problem=7
# stupid way

if __name__ == '__main__':
    primes = list()
    primes.append(2)
    current = 0

    array = list()
    for i in range(2, 200000):
        array.append(i)

    size = len(array)

    while True:
        status = False

        for i in range(primes[-1] - 2, size, primes[-1]):
            array[i] = 0

        for i in range(current, size):
            if array[i] != 0:
                primes.append(array[i])
                current = i
                status = True
                break

        if len(primes) == 10001:
            print(primes[10000])
            exit(0)

        if not status:
            break

    print(len(primes))
