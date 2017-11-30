import os
import subprocess
import sys,getopt
import optparse
from optparse import OptionParser
from argparse import ArgumentParser
from PIL import Image
import datetime


def get_date_taken(path):
	return datetime.datetime.fromtimestamp(
        int(os.stat(path).st_ctime)
    ).strftime('%Y-%m-%d %H:%M:%S')

def get_insta():
	options=get_folder_info()
	if options.i == '1':
		os.system('instaloader  profile beyhangl')
	else :
		os.system('instaloader --fast-update profile beyhangl')

def get_folder_info():
	parser = optparse.OptionParser()
	parser.add_option('-i', action="store",default="0")
	parser.add_option('-p', action="store",default="/home/kafein/Projeler/")
	options, args = parser.parse_args()

	return options
	
def detect_latest_photos():
	options=get_folder_info()
	base_path=options.p
	all_photos=os.listdir(base_path)
	for photo in all_photos:
		if photo.endswith(".jpg"):	
			update_photo_list(str(photo),base_path)	
			get_date=get_date_taken(str(base_path)+ '/'+ str(photo))
			print(get_date)

def update_photo_list(photo_name,base_path):
	f = open(str(base_path)+'/'+'processed.txt','a')
	f.write('\n' + str(photo_name))
	f.close()
def detect_new_photos():
        temp=0
	options=get_folder_info()
	base_path=options.p
	all_photos=os.listdir(base_path)
	with open(str(base_path)+'/'+'processed.txt') as g:
	 photos_list = [line.strip().replace("\n", "") for line in g]

	for pic in all_photos:
	     for line in photos_list:
                 #print(str(line) + '****'+str(pic) )
		 if str(pic) ==str(line):
		     temp=1
             if temp==0:
		if str(pic).endswith(".jpg"):
		  main_process(str(pic),base_path)
	     temp=0

def main_process(new_photo,base_path):
	print(new_photo)
	update_photo_list(new_photo,base_path)
	


	##IP code 




	##IP code
	
	
def main():
	get_insta()
	detect_latest_photos()
	detect_new_photos()
if __name__ == "__main__":
   main()


