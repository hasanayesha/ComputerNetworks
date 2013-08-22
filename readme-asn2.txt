

1. Arjun Madan: 1PI10IS021

2. Nikhil Shankar: 1PI10IS063

3. Ayesha Sabah Hasan: 1PI10IS128

Approach:

--------

1. getopt module is used to read command line arguments. If an exception occurs, it is handled.

2. The packet is created with the command line inputs and sent to the other routers using select.

3. The socket is appended to rlist, wlist and elist.

4. elist is used to store errors. If an error occurs, the socket will close, print out error occured and exit.

5. The packets are sent periodically at a time period specified by the command line arguments.

6. The nodeid’s are stored in a list. If a packet is received, the nodeid of the packet is checked to see if the packet

has already been updated in the matrix table, or the packet is discarded.

7. After a period of (timeout*nodes) seconds, if the packets received are the same, the socket closes and the matrix representing the graph is displayed on the terminal.

8. The matrix is updated after every unique packet is received.

Limitations of the Code:

------------------------

1. The program works for a maximum of 30 nodes.

2. Dynamic changes in the network cannot be handled.

3. Floating point values for node cost are not considered.

Difficulties Faced:

-------------------

1. Using select turned out to be a problem. It was understood by reading python docs and getting help from friends.

2. Link state advertisements was learnt using the CCNA modules available on the server.

3. Timeout implementation without using sleep was a little difficult, the questions posed in stackoverflow.com helped.

4. Tutorialspoint.com helped see examples of how to use dictionary.

How to Execute:

---------------

1. Go to the directory where the program is stored.

2. In command line, type:

    python asn2.py -i <node id> -t <time period for the packet to be transferred> -e < cost for the nodes in format node:cost,>

3. Test Graph:

    Nodes 4

        3        2

    [a]-----[b]--------[d]

    -       -

    -      -

    -     -

  1-    - 2

    -   -

    -  -

    - -   

    [c]

assuming a,b,c,d equal 1,2,3,4 respectively.

command lines: Router 1: python asn2.py -i 1 -t 10 -e 3:1,2:3

               Router 2: python asn2.py -i 2 -t 8 -e 3:2,1:3,4:2

               Router 3: python asn2.py -i 3 -t 5 -e 1:1,2:2

               Router 4: python asn2.py -i 4 -t 6 -e 2:2



