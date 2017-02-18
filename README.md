# secret-handshake
secret handshake with rule 30 cellular automata

Eventual goal: two parties both know a phrase that is their "secret handshake." They type this and the other party's ip into their computer. The computers verify, without leakage of information, that both parties know the "secret handshake." This is accomplished by running a 1D rule 30 cellular automaton on the handshake and a random piece of data, then comparing a line of the intersection. See illustration.



Illustration:

          ..........,,,,,,,,,,   <- Row 1, random data is '.', secret handshake is ','
         /         /\         \
        /         /  \         \ <- Data has started combining in center triangle
       /         /    \         \
      /         /      \         \
     /         /        \         \
    /         /          \         \
   /         /            \         \  <- Take line of center triangle and send for verification


The exchange goes like this:

1. Alice sends the secret data ('..........') and the line number (7)
2. Bob calculates the intersection at line 7, and sends that back.
3. Alice verifies that this matches her intersection.
4. The exchange is repeated, in reverse, so Bob can verify Alice.


##Current Features
1. Print random pretty automata (print_triangles.py)
2. Print larger automata (blocktest.py)
3. Unfinished connection work (server_client_wrapper.py)
