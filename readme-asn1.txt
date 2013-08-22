---------------------
README - Assignment 1
---------------------

Ayesha Sabah Hasan - 1PI10IS128

TEAM MEMBERS
------------

Arjun Madan - 1PI10IS021
Nikhil Shankar - 1PI10IS063


QUESTION
-----------

B1. Implement 3-party chat using UDP based on IPv6. For the program specify the command 
line arguments as follows 
 -n <name of chatter> 
 -a <ipv6 address to be used by this program> 
 -p <port number on which this program will receive chat msgs from others> 
 -d <ipv6 address of 2nd party>,<ipv6 address of 3rd party> 
 -r <port number of 2nd party>,<port number of 3rd party> 
The program will receive inputs on command line and send the same to other chat partners. 
When the program receives the input from other chat partners, it should display the same on 
console along with its id.

HOW TO EXECUTE
--------------

1. Open terminal.
2. Navigate to the directory containing Asn1.py
3. Execute the command:
python asn1.py -n<name-of-host> -a<ipv6 address of host> -p<host port number> -d<destn-address-1>,<destn-address-2> -r<destn-port-1>,<destn-port-2>
4. Execute the command three times to set up the three party chat.
5. Ctrl+D is used to terminate the program.
6. 

UNDERSTANDING
-------------

1. When the parameters are entered and no exceptions occur, the sockets are created and bound to the ports.
2. Once the connections are made, the client is notified.
3. The clients can communicate with each other by sending messages.
4. Once a message has been delivered, the client is sent a confirmation.
5. The client can quite the chat by entering ctrl+d.
6. Threads were used initially to implement the program but we were asked to use select to implement it, so er implemented the program using select.

CONSTRAINTS
-----------
1. The command line arguments take only somma seperated values as multiple inputs for a given input.

DIVISION OF WORK
----------------
 The command line arguments. Exception Handling. General Testing.
All of us worked on Client-Server logic.
The output formatting and exi logic was done by Nikhil Shankar.
The client server code using select and socket binding was done by Arjun Madan.

OUTPUT
------
System 1
tejas@pesit-To-be-filled-by-O-E-M:~/Desktop$ python Asn1.py -n Ayesha -a fe80::52e5:49ff:fe1b:ec46 -p5555 -dfe80::52e5:49ff:fe1b:f183,fe80::52e5:49ff:fe1b:f146 -r6666,7777
The parameters are: 

Name: Ayesha

ServerName: fe80::52e5:49ff:fe1b:ec46

ServerPort: 5555
fe80::52e5:49ff:fe1b:f183 fe80::52e5:49ff:fe1b:f146

Destination Addresses:
First Address fe80::52e5:49ff:fe1b:f183
Second Address fe80::52e5:49ff:fe1b:f146

Destination Ports:

 First port:  6666

 Second port:  7777
Client Socket has been created.
Server Socket has been created.
hi
Message sent
Nikhil@fe80::52e5::49ff:f31b:f183 says: hi
Arjun@fe80::52e5:49ff:fe1b:f146 says: Hi!
Nikhil@fe80::52e5::49ff:f31b:f183 says: This works!
across three systems!
Message sent
Arjun@fe80::52e5:49ff:fe1b:f146 says: Test successful
Nikhil@fe80::52e5::49ff:f31b:f183 says: bye
Arjun@fe80::52e5:49ff:fe1b:f146 says: Wait!
bye
Message sent
Arjun@fe80::52e5:49ff:fe1b:f146 says: We have to fill up the screen
Nikhil@fe80::52e5::49ff:f31b:f183 says: Why?
Arjun@fe80::52e5:49ff:fe1b:f146 says: Screenshot
Genius!
Message sent
Nikhil@fe80::52e5::49ff:f31b:f183 says: Oh scrYes.
Nikhil@fe80::52e5::49ff:f31b:f183 says: Okay bye.
Arjun@fe80::52e5:49ff:fe1b:f146 says: Bye!

