#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    r = range(100)
    for b in r:
        for k in r:
            for t in r:
                if b + k + t == 100 and (10 * b) + (5 * k) + (t * 0.5) == 100:
                    print("Быков:", b)
                    print("Коров:", k)
                    print("Телят:", t)
                    print(" ")
