import os, sys

cov_filename = sys.argv[1]#coverage_file
out_filename = sys.argv[2]

out_file_object = open(out_filename,'w')

def outputFile(preName):
	ave = float(float(cov)/float(count))
	out_file_object.write(preName  + '\t' + str(ave) + '\n')


with open(cov_filename) as file_object:
	preName = ""
	count = 0
	cov = 0
	for line in file_object:
		if line.startswith("#"):
			continue
		else:
			line = line.rstrip("\n")
			lineList = line.split("\t")
			bin = lineList[0].split("_")[1]
			if bin != preName:#第一次bin与preName不符，
				if preName != "":
					outputFile(preName)
				preName = bin
				count = 0
				cov = 0
			count = count + 1
			cov = cov + float(lineList[3])
	outputFile(preName)

file_object.close()
out_file_object.close()