from MEC_Lib import text2bin, bin2text, hex2rgb
from PIL import Image
import numpy
import cv2
from math import sqrt
import os


utf8 = [chr(i) for i in range(0x110000)][1:]
rgb_vals = [hex2rgb('0'*(6-len(hex(i).replace('0x', '')))+str(hex(i).replace('0x', ''))) for i in range(0x110000)][1:]


def text2image(text):
	size = int(sqrt(len(text)))+1
	size = (size, size)

	image = Image.open('image.png') # cv2.imread('image.png', 1)
	image = numpy.array(image, dtype=numpy.uint8)
	image = cv2.resize(image, size)

	pixel_counter = 0
	for ri, row in enumerate(image):		# ri -> row index
		for pi, pixel in enumerate(row):	# pi -> pixel index
			if pixel_counter < len(text):
				image[ri][pi] = list(rgb_vals[utf8.index(text[pixel_counter])])
				pixel_counter += 1
			else:
				image[ri][pi] = [0, 0, 0]
	cv2.imwrite('result.png', image)

def image2text(image):
	image = numpy.array(Image.open(image), dtype=numpy.uint8)[:, :, [2, 1, 0]]
	text = ''
	for row in image:
		for pixel in row:
			if sum(pixel) != 0:
				text += utf8[rgb_vals.index(tuple(pixel))]
	return text


while True:
	command = input(':> ')
	if command.startswith('encode'):
		text = ' '.join(command.split()[1:])
		print(text)
		try:
			text2image(text)
			print('Done !')
		except: print('Error')

	elif command.startswith('decode'):
		file = command.split()[1]
		try:
			print(image2text(file))
			print('Done !')
		except: print('Error')

	elif command == 'dir':
		for root, dirs, files in os.walk('./'):
			print('files:\n\t'+'\n\t'.join(files))
			print('dirs:\n\t'+'\n\t'.join(dirs))
			break

	elif command == 'exit': exit()

	print('='*100)