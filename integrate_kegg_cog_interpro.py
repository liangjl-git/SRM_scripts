from collections import defaultdict
import os, sys, getopt

nameDict = defaultdict(list)

kegg_filename = sys.argv[1]
cog_filename = sys.argv[2]
interpro_filename = sys.argv[3]
out_filename = sys.argv[4]


for line in open(kegg_filename):
	line = line.rstrip("\n")
	seqName = line.split("\t")[0]
	kegg = line.split()[-1]
	if "K" in kegg:
		nameDict[seqName].append(kegg)
	else:
		nameDict[seqName].append("noKEGG")

line_count = 0
for line in open(cog_filename):
	line_count = line_count + 1
	if line_count == 1:
		continue
	seqName = line.split("\t")[0]
	nameDict[seqName].append(line.split("\t")[-2])

for line in open(interpro_filename):
	seqName = line.split("\t")[0]
	nameDict[seqName].append(line.split("\t")[4])

with open(out_filename,'w') as outHandle:
	for seqName in nameDict:
		outHandle.write(seqName+'\t'+'\t'.join(nameDict[seqName])+'\n')
outHandle.close()
