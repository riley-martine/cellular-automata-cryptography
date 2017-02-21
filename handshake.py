#!/usr/bin/env python3
""" secret handshake made with class 4 cellular automata"""

import random
import sys
import functions
import rules
import time
from server_client_wrapper import serverThread, clientThread


def random_wordlist(length):
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()

    random_words = []
    for _ in range(length):
        random_words.append(random.choice(words))

    random_words = [random.choice(words) for _ in range(length)]

    return random_words


if __name__ == "__main__":
    mode = input("Enter 'e' to enter a secret, or 'g' to generate one: ")
    if mode == 'e':
        secret = input("Enter the secret: ").replace(' ', '').lower()
        secret = string_to_bin(secret)
    elif mode == 'g':
        length = int(input("How many words should the secret be?: "))
        secret = ' '.join(random_wordlist(length))
        print("Your secret is:\n" + secret)
        secret = string_to_bin(secret.replace(' ', '').lower())
        sys.exit(0)
    else:
        print("Unknown command. Exiting.")
        sys.exit(0)

    iters = 0
    while iters == 0:
        iters = int(input("What is the line you have agreed on?: "))

    rows = functions.get_rows(secret, rules.RuleList(30).rules, iters)
    last_row = rows[-1]

    server_thread = serverThread(last_row)
    server_thread.start()
    time.sleep(1)

    ip = input("Server ip: ")
    client_thread = clientThread(ip, last_row)
    client_thread.start()
