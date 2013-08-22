from threading import Thread
import getopt
import time
import sys
from socket import *
from select import *

try:
	opts, args=getopt.getopt(sys.argv[1:],"n:a:p:d:r:")
	if len(sys.argv)<2:
		print '\nNot enough arguments!'
		print '\nRun program again and specify command line parameters in the following order'
		print '\n-n <host name> -a <Server Name> -p <port number of the client> -d <Destination address of the other two clients> -r <Port numbers of the destination clients in the same order>'   
		sys.exit(1)
	if len(sys.argv)<5:
	    print '\nNot enough arguments!'
            print '\nRun program again and specify command line parameters in the following order'
	    print '\n-n <host name> -a <Server Name> -p <port number of the client> -d <Destination address of the other two clients> -r <Port numbers of the destination clients in the same order>'   
	    sys.exit(1)
except getopt.GetoptError, err:
	print str(err)

print 'The parameters are: '
for o,arg in opts:
	
	if o=="-n":
		name=arg
		print '\nName:',arg
	
	elif o=="-a":
		serverName=arg
		print '\nServerName:',arg
	
	elif o=="-p":
		try:
			serverPort=int(arg)
			print '\nServerPort:',arg
		except 	ValueError,v:
			print v
			sys.exit(1)

	elif o=="-d":
		add=arg
		twoadd=add.split(',')
		add1=twoadd[0]
		add2=twoadd[1]
		print add1,add2
		print '\nDestination Addresses:'
		print 'First Address',add1
		print 'Second Address',add2
	
	elif o=="-r":
		destnPort=arg
		destnPort=destnPort.split(",")
		try:
			dPort1=int(destnPort[0])
			dPort2=int(destnPort[1])
			if((dPort1 >0 and dPort1< 65536 ) and (dPort2 > 0 and dPort2 <65536)):
				print '\nDestination Ports:'
				print '\n First port: ',dPort1
				print '\n Second port: ',dPort2
		except ValueError,v:
				print v
				sys.exit(1)


sockList = []
sockList.append(sys.stdin)
try:

	clientSocket = socket(AF_INET6, SOCK_DGRAM)
except socket.error, msg:
		sys.stderr.write("[ERROR] %s\n" % msg[1])
		sys.exit(1)
print 'Client Socket has been created.'
sockList.append(clientSocket)
try:
	serverSocket = socket(AF_INET6, SOCK_DGRAM)
except socket.error, msg:
		sys.stderr.write("[ERROR] %s\n" % msg[1])
		sys.exit(1)
print 'Server Socket has been created.'

try:	
	serverSocket.bind(('', int(serverPort)))
except error, msg:
		sys.error.write("\n[ERROR] %s" %msg[1])
		print 'The socket couldn\'t be bound.'
		sys.exit(1)
try:
	sockList.append(serverSocket)
except:
	print 'Error Occured when appending to Socket.'

while True:
    rlist, wlist, elist = select(sockList, [], sockList)
    if not (rlist, wlist, elist):
        print "No sockets are currently ready.\n"
    for rsock in rlist:
        if rsock == serverSocket:
		message, clientAddr = serverSocket.recvfrom(2048)
    		print message

        if rsock == sys.stdin:
		message = name + "@" + serverName +" says: "
		try:		
			msgdata = raw_input('')
		except:
			sys.exit(1)
		message = message + msgdata		
		try:
			clientSocket.sendto(message, (add1, int(dPort1)))
			clientSocket.sendto(message, (add2, int(dPort2)))
		except error, msg:
			sys.error.write("\n[ERROR] %s" %msg[1])
			print 'Try again later.'
			sys.exit(1)
		print "Message sent"		
clientSocket.close()
