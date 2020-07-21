import sys

def pull_data():
	data = []
	peaks = []
	with open("malevsfemalepool.psl", 'r') as macs_data:
		for line in macs_data:
			if line.startswith("#"):
				continue
			else:
				data += line.split()
		match=data[0::21]
		mismatch=data[1::21]
		repmatch=data[2::21]
		Ns=data[3::21]
		Qgap=data[4::21]
		qgapbases=data[5::21]
		Tgapcount=data[6::21]
		Tgapbases=data[7::21]
		strand=data[8::21]
		Qname=data[9::21]
		Qsize=data[10::21]
		Qstart=data[11::21]
		Qend=data[12::21]
		Tname=data[13::21]
		Tsize=data[14::21]
		Tstart=data[15::21]
		Tend=data[16::21]
		blockcount=data[17::21]
		blocksizes=data[18::21]
		qStarts=data[19::21]
		tStarts=data[20::21]
		for index,value in enumerate(match):
			peaks.append(value)
			peaks.append(mismatch[index])
			peaks.append(repmatch[index])
			peaks.append(Ns[index])
			peaks.append(Qgap[index])
			peaks.append(qgapbases[index])
			peaks.append(Tgapcount[index])
			peaks.append(Tgapbases[index])
			peaks.append(strand[index])
			peaks.append(Qname[index])
			peaks.append(Qsize[index])
			peaks.append(Qstart[index])
			peaks.append(Qend[index])
			peaks.append(Tname[index])
			peaks.append(Tsize[index])
			peaks.append(Tstart[index])
			peaks.append(Tend[index])
			peaks.append(blockcount[index])
			peaks.append(blocksizes[index])
			peaks.append(qStarts[index])
			peaks.append(tStarts[index])
	return peaks 
	
def pull_data2():
	data = []
	XY = []
	with open("XorYmale.all.psl", 'r') as macs_data:
		for line in macs_data:
			if line.startswith("#"):
				continue
			else:
				data += line.split()
		match=data[0::21]
		mismatch=data[1::21]
		repmatch=data[2::21]
		Ns=data[3::21]
		Qgap=data[4::21]
		qgapbases=data[5::21]
		Tgapcount=data[6::21]
		Tgapbases=data[7::21]
		strand=data[8::21]
		Qname=data[9::21]
		Qsize=data[10::21]
		Qstart=data[11::21]
		Qend=data[12::21]
		Tname=data[13::21]
		Tsize=data[14::21]
		Tstart=data[15::21]
		Tend=data[16::21]
		blockcount=data[17::21]
		blocksizes=data[18::21]
		qStarts=data[19::21]
		tStarts=data[20::21]
		for index,value in enumerate(match):
			XY.append(value)
			XY.append(mismatch[index])
			XY.append(repmatch[index])
			XY.append(Ns[index])
			XY.append(Qgap[index])
			XY.append(qgapbases[index])
			XY.append(Tgapcount[index])
			XY.append(Tgapbases[index])
			XY.append(strand[index])
			XY.append(Qname[index])
			XY.append(Qsize[index])
			XY.append(Qstart[index])
			XY.append(Qend[index])
			XY.append(Tname[index])
			XY.append(Tsize[index])
			XY.append(Tstart[index])
			XY.append(Tend[index])
			XY.append(blockcount[index])
			XY.append(blocksizes[index])
			XY.append(qStarts[index])
			XY.append(tStarts[index])
	return XY 
	
def compare1():
	mvf=pull_data()
	xandy=pull_data2()
	match=mvf[0::21]
	mismatch=mvf[1::21]
	repmatch=mvf[2::21]
	Ns=mvf[3::21]
	Qgap=mvf[4::21]
	qgapbases=mvf[5::21]
	Tgapcount=mvf[6::21]
	Tgapbases=mvf[7::21]
	strand=mvf[8::21]
	Qname=mvf[9::21]
	Qsize=mvf[10::21]
	Qstart=mvf[11::21]
	Qend=mvf[12::21]
	Tname=mvf[13::21]
	Tsize=mvf[14::21]
	Tstart=mvf[15::21]
	Tend=mvf[16::21]
	blockcount=mvf[17::21]
	blocksizes=mvf[18::21]
	qStarts=mvf[19::21]
	tStarts=mvf[20::21]	
	bmatch=xandy[0::21]
	bmismatch=xandy[1::21]
	brepmatch=xandy[2::21]
	bNs=xandy[3::21]
	bQgap=xandy[4::21]
	bqgapbases=xandy[5::21]
	bTgapcount=xandy[6::21]
	bTgapbases=xandy[7::21]
	bstrand=xandy[8::21]
	bQname=xandy[9::21]
	bQsize=xandy[10::21]
	bQstart=xandy[11::21]
	bQend=xandy[12::21]
	bTname=xandy[13::21]
	bTsize=xandy[14::21]
	bTstart=xandy[15::21]
	bTend=xandy[16::21]
	bblockcount=xandy[17::21]
	bblocksizes=xandy[18::21]
	bqStarts=xandy[19::21]
	btStarts=xandy[20::21]
	x=0
	with open("malevsfemaleonXY", 'a') as out:
		while x < len(match):
			for index,value in enumerate(bmatch):
				if str(Qname[x]) == str(bQname[index]):
					out.write(str(match[x]) + '\t' + str(mismatch[x]) + '\t' + str(repmatch[x]) + '\t' + str(Ns[x]) + '\t' + str(Qgap[x]) + '\t' + str(qgapbases[x]) + '\t' + str(Tgapcount[x]) + '\t' + str(Tgapbases[x]) + '\t' + str(strand[x]) + '\t' + str(Qname[x]) + '\t' + str(Qstart[x]) + '\t' + str(Qend[x]) + '\t' + str(Tname[x]) + '\t' + str(Tstart[x]) + '\t' + str(Tend[x]) + '\t' + str(blockcount[x]) + '\t' + str(blocksizes[x]) + '\t' + str(qStarts[x]) + '\t' + str(tStarts[x]) + '\n')
			x+=1	

		
	

compare1()
