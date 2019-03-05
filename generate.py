#!/usr/bin/env python

import sys
import os

if len(sys.argv)<2:
    print("Usage: $python generate.py [filename]")
    exit()
filename = sys.argv[1]
fin = open(filename)
cnt = 0
ffmpeg_file = open("ffmpeg.txt","w")
for line in fin:
    line = line.strip()
    outfile = str(cnt)+".aiff"
    cmd = "say -v Thomas " + line + " -o "+ outfile
    print(cmd)
    os.system(cmd)
    cnt = cnt+1
    ffmpeg_file.write("file "+"'"+outfile+"'"+"\n")

ffmpeg_file.close()
os.system("ffmpeg -f concat -i ffmpeg.txt -c copy output.aiff")
os.system("lame -m m output.aiff output.mp3")