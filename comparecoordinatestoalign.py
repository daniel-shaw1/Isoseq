import sys

def pull_data():
	data = []
	peaks = []
	with open("str1random.xls", 'r') as macs_data:
		for line in macs_data:
			if line.startswith("#"):
				continue
			else:
				data += line.split()
		chr=data[0::16]
		start=data[1::16]
		stop=data[2::16]
		XIX=data[3::16]
		ID=data[4::16]
		Length=data[5::16]
		Mismatch=data[6::16]
		Gap=data[7::16]
		Qstart=data[8::16]
		Qend=data[9::16]
		Xstart=data[10::16]
		Xend=data[11::16]
		Evalue=data[12::16]
		value=data[13::16]
		Maplength=data[14::16]
		Divergence=data[15::16]
		for index,value in enumerate(chr):
			peaks.append(value)
			peaks.append(start[index])
			peaks.append(stop[index])
			peaks.append(XIX[index])
			peaks.append(ID[index])
			peaks.append(Length[index])
			peaks.append(Mismatch[index])
			peaks.append(Gap[index])
			peaks.append(Qstart[index])
			peaks.append(Qend[index])
			peaks.append(Xstart[index])
			peaks.append(Xend[index])
			peaks.append(Evalue[index])
			peaks.append(Maplength[index])
			peaks.append(Divergence[index])
	return peaks


def pull_data2():
	data = []
	peaks = []
	with open("str1Xalignment.bed", 'r') as macs_data:
		for line in macs_data:
			if line.startswith("#"):
				continue
			else:
				data += line.split()
		chr=data[0::3]
		start=data[1::3]
		stop=data[2::3]
		for index,value in enumerate(chr):
			peaks.append(value)
			peaks.append(start[index])
			peaks.append(stop[index])

	return peaks	
	
	
	
def compare1():
	blast=pull_data()
	align=pull_data2()
	chr=blast[0::15]
	start=blast[1::15]
	stop=blast[2::15]
	XIX=blast[3::15]
	ID=blast[4::15]
	Length=blast[5::15]
	Mismatch=blast[6::15]
	Gap=blast[7::15]
	Qstart=blast[8::15]
	Qend=blast[9::15]
	Xstart=blast[10::15]
	Xend=blast[11::15]
	Evalue=blast[12::15]
	Maplength=blast[13::15]
	Divergence=blast[14::15]		
	chrb=align[0::3]
	startb=align[1::3]
	stopb=align[2::3]
	x=0
	with open("blastinalignmentstr1", 'a') as out:
		while x < len(chrb):
			for index,value in enumerate(chr):
				if int(Xstart[index]) >= int(startb[x]) and int(Xend[index]) <= int(stopb[x]):
					out.write(str(chr[index]) + '\t' + str(start[index]) + '\t' + str(stop[index]) + '\t' + str(XIX[index]) + '\t' + str(ID[index]) + '\t' + str(Length[index]) + '\t' + str(Mismatch[index]) + '\t' + str(Gap[index]) + '\t' + str(Qstart[index]) + '\t' + str(Qend[index]) + '\t' + str(Xstart[index]) + '\t' + str(Xend[index]) + '\t' + str(Evalue[index]) + '\t' + str(Maplength[index]) + '\t' + str(Divergence[index]) + '\t' + str(startb[x]) + '\t' + str(stopb[x]) + '\n')

			x+=1	

		
	

compare1()


        
 
