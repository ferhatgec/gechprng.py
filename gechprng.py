# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
# gechprng[dot]py - small & fast prng algorithm
#
# github.com/ferhatgec/gechprng.py
# github.com/ferhatgec/gechprng
#

class gechprng:
    def __init__(self):
        self.__seed, self.__bits = 1, 1

    def feed(self, seed):
        self.__seed = seed

    def generate(self):
        self.__bits ^= (self.__seed >> 1) | (self.__seed >> 2) | (self.__seed >> 3) | (self.__seed >> 4)
        self.__bits  = (self.__bits >> 1) | (self.__bits >> 2) | (self.__bits >> 3) | (self.__bits >> 4)
        self.__bits *= (self.__bits >> 1) | (self.__seed >> 2) | (self.__bits >> 3) | (self.__seed >> 4)
        self.__bits |= (self.__seed << 1) ^ (self.__seed << 2) ^ (self.__seed << 3) ^ (self.__seed << 3)

        return self.__bits << 32