input = './api/md'
output = './api'
image_dir = './api/md/media'

from subprocess import call
import os

for filename in os.listdir(input):
	if filename.endswith('.md'):
		print("Converting " + filename + " to RST")
		call(["pandoc", "-s", input + '/' + filename, "-o", output + '/' + filename[0:-3] + '.rst'])

call(["cp", '-r', image_dir, output + "/media"])