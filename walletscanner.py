import json
import urllib.request, urllib.error, urllib.parse
import time
import sys

def Wallet (addr):
	"""Check address for duplicated R Values."""

	# TODO: add BCI API check address

	print("ADDRESS-SCANNING: ")
	
	urladdr = 'https://blockchain.info/address/%s?format=json&offset=%s'


	addrdata = json.load(urllib.request.urlopen(urladdr % (addr, '0')))
	ntx = addrdata['n_tx']
	print("Data for Wallet Address: " + str(addr) + " has " + str(addrdata['n_tx']).center(6) + "Tx%s" % 's'[ntx==1:])
	#print "number of txs: " + str(addrdata['n_tx'])


	txs = []
	for i in range(0, ntx//50 + 1):
		sys.stderr.write("Fetching Txs from offset\t%s\n" % str(i*50))
		jdata = json.load(urllib.request.urlopen(urladdr % (addr, str(i*50))))
		txs.extend(jdata['txs'])	

	assert len(txs) == ntx
	addrdata['txs'] = txs


	y = 0
	inputs = []
	while y < ntx:	
		zy = 0
		while zy < addrdata['txs'][y]['vin_sz']:
			inputs.append(addrdata['txs'][y]['inputs'][zy]['script'])
			zy += 1
		y += 1

	xi = 0
	zi = 1
	lenx = len(inputs)
	alert = 0
	
	bad = []
	while xi < lenx-1:
		x = 0
		while x < lenx-zi:
			if inputs[xi][10:74] == inputs[x+zi][10:74]:
				print("Reused R-Value: ")
				print(inputs[x+zi][10:74])
				bad.append((int(x), str(inputs[x+zi][10:74])))
				alert += 1
			x += 1
			zi += 1
		xi += 1


	if alert < 1:
		print("Good public Key. No Issues.")
	else:
		print("Address %s has %d reused R value%s!" % (addr, len(bad), "s"[len(bad)==1:]))
		return bad
		
if __name__ == '__main__':
	from sys import argv
	print("""SCAN ADDR""")
	if len(argv) == 1:
		addr = input("type address:  ")
	elif len(argv) == 2 and isinstance(argv[1], str):
		addr = str(argv[1])
	def wallet(addr)
	

	
