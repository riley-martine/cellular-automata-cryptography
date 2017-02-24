#!/usr/bin/env python3

import random

random.seed()


class Automaton():

    def __init__(self, key):
        self.key = key
        self.sequence = list(key)

    def update(self):
        last = tuple(self.sequence)
        current = [0 for k in last]
        current[0] = (last[-1] + last[0] + last[1] + last[0] * last[1]) % 2
        current[-1] = (last[-2] + last[-1] + last[0] + last[-1] * last[0]) % 2
        for i in range(1, len(last) - 1):
            current[i] = (last[i - 1] + last[i] + last[i + 1] +
                          last[i] * last[i + 1]) % 2
        self.sequence = current

    def get_bin_string(self):
        string = ''
        for k in self.sequence:
            string += str(k)
        return string

    def getCipherText(self, text):
        cipherTextChars = []
        buf = ' '.join(format(ord(x), 'b') for x in text)
        buf = buf.split()
        sequence = self.get_bin_string()
        cipherTextChars.append(int(sequence, 2) ^ int(buf[0], 2))
        for char in buf[1:]:
            self.update()
            sequence = self.get_bin_string()
            cipherTextChars.append(int(sequence, 2) ^ int(char, 2))
        cipherText = ''.join(chr(x) for x in cipherTextChars)
        return cipherText

    def getPlainText(self, text):
        plainTextChars = []
        buf = ' '.join(format(ord(x), 'b') for x in text)
        buf = buf.split()
        sequence = self.get_bin_string()
        plainTextChars.append(int(sequence, 2) ^ int(buf[0], 2))
        for char in buf[1:]:
            self.update()
            sequence = self.get_bin_string()
            plainTextChars.append(int(sequence, 2) ^ int(char, 2))
        plainText = ''.join(chr(x) for x in plainTextChars)
        return plainText

    def reset(self):
        self.sequence = [k for k in self.key]
