# cellular-automata-cryptography

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6ac9d62513a040dea8cf29489322b394)](https://www.codacy.com/app/rmartine/cellular-automata-cryptography?utm_source=github.com&utm_medium=referral&utm_content=riley-martine/cellular-automata-cryptography&utm_campaign=badger)

block cipher with class 4 cellular automata

The exchange currently goes like this:

0. Alice and Bob securely agree on a key, of length >8, comprised of ones and zeros
1. Alice encodes the plaintext with the key and sends the ciphertext
2. Bob calculates the plaintext from the ciphertext and key.
3. That's it. The key is the seed.

##Current Features
0. Send secret messages (s\_c\_gui.py)
1. Print random pretty automata (print\_triangles.py)
2. Print larger automata (blocks.py)
3. Generate defect cones for analysis (big.py) (analyze these with https://github.com/riley-martine/lyapunov-ca-gen)

