import Image
import os
from os.path import splitext, exists
from os import mkdir
import sys, getopt


def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print 'Please specify input file: split_image.py -i <inputfile>'

    if len(opts) == 0:
        print 'Please specify input file: split_image.py -i <inputfile>'
        sys.exit(2)

    for opt, arg in opts:
      if opt == '-h':
         print 'split_image.py -i <inputfile>'
         sys.exit(2)
      elif opt in ("-i", "--ifile"):
         inputfile = arg

    print inputfile

    height=128
    width=128
    start_num=0
            
    dir_name = splitext(inputfile)[0]
    out_name = dir_name + "_separated"
    if not exists (out_name):
        mkdir(out_name)

    for k,piece in enumerate(crop(inputfile,height,width),start_num):
        img=Image.new('RGB', (height,width), 255)
        img.paste(piece)
        path=os.path.join(out_name,"IMG-%s.png" % k)
        img.save(path)


if __name__=='__main__':
    main(sys.argv[1:])

