from collections import defaultdict
import os, sys, getopt


ko_filename = sys.argv[1]
bbmap_filename = sys.argv[2]
out_filename = sys.argv[3]

out_file_object = open(out_filename,'w')

ko2seq = {}
with open(ko_filename) as file_object:
	for line in file_object:
		line = line.rstrip("\n")
		ko = line.split("\t")[-1]
		seq = line.split("\t")[0]
		ko2seq[seq] = ko
file_object.close()

with open(bbmap_filename,"r") as file_object:
	for line in file_object:
		if line.startswith("#"):
			out_file_object.write(line)
		else:
			line = line.rstrip("\n")
			gene = line.split("\t")[0]
			if gene in ko2seq:
				out_file_object.write(line + ko2seq[gene] +'\n')
file_object.close()
out_file_object.close()
