#!/usr/bin/env python
# encoding: utf-8
"""
export_privatepics.py
Created by Magnus Wahlberg on 2014-03-27.
V0.0.1

"""

import sys
import sqlite3
import imghdr

def get_image_ext(data):
    try:
        return imghdr.what(None, data)
        print image_type
    except IOError, E:
        return False

def export_images(ppstorage):
	conn = sqlite3.connect(ppstorage)
	cursor = conn.cursor()
	
	cursor.execute('SELECT ZDATA FROM ZORIGINALIMAGE')
	blobs = cursor.fetchall()
	for idx, image in enumerate(blobs):
			image_ext = get_image_ext(image[0])
			if image_ext:
				image_file =  "pp_image_" + str(idx) + "." + image_ext
				with open(image_file, "wb") as output_file:
					print image_file
					output_file.write(image[0])
			else:
				print "Not an image file..."
	
	cursor.close()
	conn.close()


def main():
	try:
		pp_db = sys.argv[1]
	except:
		print "Please a privatepics db" 
		sys.exit(1)

	export_images(pp_db)

if __name__ == '__main__':
	main()
