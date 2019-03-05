#!/usr/bin/env python

import sys
import os
import subprocess

if len(sys.argv)<2:
    print("Usage: $python generate.py [filename]")
    exit()
filename = sys.argv[1]
fin = open(filename)
cnt = 0
ffmpeg_file = open("ffmpeg.txt","w")
for line in fin:
    line = line.strip()
    fr = line.split(",")[0]
    jp = line.split(",")[1]
    outfile_fr = str(cnt)+"_fr.aiff"
    outfile_jp = str(cnt)+"_jp.aiff"
    cmd_fr = "say -v Thomas " + fr + " -o "+ outfile_fr
    cmd_jp = "say -v Kyoko " + jp + " -o "+ outfile_jp
    print(cmd_fr)
    print(cmd_jp)
    os.system(cmd_fr)
    os.system(cmd_jp)
    status_fr, _ = subprocess.getstatusoutput("ls "+outfile_fr)
    status_jp, _ = subprocess.getstatusoutput("ls "+outfile_jp)
    if status_fr<1 && status<jp<1:
        ffmpeg_file.write("file "+"'"+outfile_fr+"'"+"\n")
        ffmpeg_file.write("file "+"'"+outfile_jp+"'"+"\n")
    cnt = cnt+1

ffmpeg_file.close()
os.system("ffmpeg -f concat -i ffmpeg.txt -c copy output.aiff")
os.system("lame -m m output.aiff output.mp3")