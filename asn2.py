import sys
from socket import *
from select import *
import getopt
import time

try:
	opts, args=getopt.getopt(sys.argv[1:],"i:t:e:")
	if len(sys.argv)<3:
		print '\nNot enough arguments!'
		print '\nRun program again and specify command line parameters in the following order'
		print '\n-i node id -t time limit -e <neighbour cost list>'   
		sys.exit(1)

except getopt.GetoptError, err:
	print 'Command Line error.'
	print str(err)

for o,arg in opts:
	
	if o=="-i":
		ID=arg
		print '\nNode ID: ',arg
	
	elif o=="-t":
		tim=arg
		print '\nTime: ',arg
	

	elif o=="-e":
		temp=arg		
		edgeList = []
		node = []
		edgeList=temp.split(',')
		print "Edge list: ",
		for i in range(0,len(edgeList)):
			node=edgeList[i].split(":")
			print node,
		print ""


def matrixmaker(nodecost, nodeid, matrix):
	node1=[]
	cost=[]
	sepnc=[]
	finalnode=[]
	finalcost=[]
	ncsplit=nodecost.split(",")
	for j in range(len(ncsplit)):
		sepnc=ncsplit[j].split(":")
		node1.append(int((sepnc[0])));
		cost.append(sepnc[1]);
	dt=dict()
	for i in range(len(node1)):
		key,value =ncsplit[i].split(':')
		dt[int(key)]=int(value)
	high=max(node1)
	
	for i in range(0,high):
		matrix[i][i]=0;
	
	for i in range(len(node1)):
		if dt.has_key(node1[i]):
			matrix[int(nodeid)-1][node1[i]-1]=dt[node1[i]]
		else:
			continue
	return matrix




nodeList = []
timeList = []
costList = []
packet=[]
nodecost={}
t = time.time()
message = str(ID) + '>' + str(t) + '>' + str(temp)
new=[]
tnew=[]	

for i in range(len(edgeList)):
	new=edgeList[i].split(':')
	tnew.append(new[0])

try:
	sock_lsa=socket(AF_INET,SOCK_DGRAM)
except socket.error, msg:
	sys.stderr.write("[ERROR] %s\n" % msg[1])
	sys.exit(1)
print 'Socket has been created.'

host='127.0.0.1'
port=50000+int(ID)

try:
	sock_lsa.bind((host,port))
except error, msg:
	sys.error.write("\n[ERROR] %s" %msg[1])
	print 'The socket couldn\'t be bound.'
	sys.exit(1)

sockList = []
try:
	sockList.append(sock_lsa)
except error, msg:
	sys.error.write("\n[ERROR] %s" %msg[1])
	print 'The socket couldn\'t be appended.'
	sys.exit(1)

end = time.time()+15 #to allow all terminals to be setup before initial sending

high = 30
matrix = [[999 for x in xrange(high)] for x in xrange(high)]
timeout = time.time()+50
	
m1 = 0
m2 = int(ID)
m3 = int(max(m1,m2))
			
while True:

	try:
		rlist,wlist,elist=select(sockList, sockList, sockList)
	except KeyboardInterrupt:
    		print ''
    		sock_lsa.close()
    		sys.exit()

	if wlist:
		temp_time = time.time()
    		if temp_time > end:
				for i in tnew:
					port = 50000+int(i)
					addr = '127.0.0.1'
					try:
						sock_lsa.sendto(message,(addr,port))
					except error, msg:
						sys.error.write("\n[ERROR] %s" %msg[1])
						print 'The data couldn\'t be sent.'
						sys.exit(1)
				end = end + int(tim)
		if (time.time() - timeout) > int(tim)*m3:
			print "**************"
			print "Final matrix: "
			print "**************"
			for i in range(0,m3):
				for j in range(0, m3):
					print matrix[i][j], " ",
				print '\n'
			sys.exit()


	if rlist:
		msg, clientAddr = sock_lsa.recvfrom(2048)
		packet=msg.split('>')
#		print msg
		flag=False
		for i in range(len(nodeList)):
			if packet[0]==nodeList[i]:
				#Packet Being discarded.'
				flag=True
				
		if(flag==False):
			nodeList.append(packet[0])
			timeList.append(packet[1])
			costList.append(packet[2])
			matrix = matrixmaker(packet[2], packet[0], matrix)
			m1 = int(max(nodeList))
			m2 = int(ID)
			m3 = int(max(m1,m2))
				
			for i in tnew:
				sock_lsa.sendto(msg, ('127.0.0.1', 50000+int(i)))

			print "Changed matrix:"
			for i in range(0,m3):
				for j in range(0, m3):
					print matrix[i][j], " ",
				print '\n'
			timeout = time.time()


	if elist:
		sock_lsa.close()
		print 'Error Occured. The socket has been closed and the program is exiting.'
		sys.exit()

