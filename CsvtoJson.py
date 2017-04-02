#-*- coding:utf8 -*-
import csv
import json
from csv import DictReader

class CsvtoJson():
	def __init__(self,filename):  #Input filename first
		self.filename=filename
	def PrintcsvField(self): #Show you fieldname
		array=list()
		with open(self.filename) as csvfiles:
			data=DictReader(csvfiles)
			for row in data.fieldnames:
				array.append(row)
		csvfiles.close()
		print(array)


	def CsvtoJson(self):
		file=self.filename
		jsonfilename=file.split('.')[0]+'.json'#Use input filename to split and make new json file name
		jsonfile=open(jsonfilename,'w')
		with open(file) as csvfile:
			reader = DictReader(csvfile) #make csvfile to dict format
			for row in reader:
				#use ensure_ascii to prevent unicode,indent  make page good  
				json.dump(row, jsonfile, sort_keys=True,indent=4, separators=(',', ': '),ensure_ascii=False)
		csvfile.close()
		print("The Json file has done")
		
			
		




if  __name__ ==  "__main__" :
	test=CsvtoJson("yiland_a.csv")
	test.PrintcsvField()
	test.CsvtoJson()
