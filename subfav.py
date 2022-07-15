#!/usr/bin/python3
import argparse
import subprocess as ss
import requests, mmh3, codecs
parser=argparse.ArgumentParser(description="This is subdomain finder")
parser.add_argument("-d",type=str,help="provide domain",required=True)
args = parser.parse_args()

def subfind():
	a = args.d
	h = "subfinder -d {} -silent".format(a)
	b = ss.getoutput(h)
	print("-------------------")
	print("Subdomains")
	print("-------------------")
	print(b)
	with open("subdomains.txt","w") as f:
		f.write(b)
def alive():
	data = open("subdomains.txt", "r")
	subs = data.readlines()
	data.close()
	f = open("alive.txt","a")
	print("\n-------------------")
	print("--Alive Subdomain--")
	print("------------------")
	for i in subs:
		try:
			u = "http://"+i.strip()
			u_statuscode = requests.get(u,timeout=10).status_code
			s = "https://"+i.strip()
			s_statuscode = requests.get(s,timeout=10).status_code
			print(u, u_statuscode)
			print(s, s_statuscode)
			if int(u_statuscode) == 200:
				f.write(u + " " + "[200]\n")
			elif int(s_statuscode) == 200:
				f.write(s + " " + "[200]\n")
		except:
			pass
	f.close()

def favhash():
	f = open("alive.txt", "r")
	alive = f.readlines()
	f.close()

	for fav in alive:
		d = fav.split()[0].strip() + "/favicon.ico"

		with open("favicon.txt", "a") as favicon:
			ff = codecs.encode(requests.get(d).content, "base64")
			hash = mmh3.hash(ff)
			cc = d + str(hash) + '\n'
			favicon.write(cc)
			print("favicon hash")
			print("--------------------------")
			print(cc)
			print("--------------------------")
		favicon.close()


subfind()
alive()
favhash()
