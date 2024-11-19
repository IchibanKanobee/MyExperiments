import os, shutil
import subprocess


MOVIE_PATH = 'render/'

os.chdir(MOVIE_PATH)
subprocess.call(['ffmpeg', '-i', 'model_%02d_%d.png', '-start_number', '0', '-vf', 'fps=25', 'output.avi'])

#ffmpeg -pattern_type glob -i "*.png" -vf fps=25 output.avi
