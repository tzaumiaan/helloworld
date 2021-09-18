import os
import glob
import sys

curdir = os.getcwd()
m4adir = os.path.join(curdir, sys.argv[1])
assert os.path.exists(m4adir)
os.chdir(m4adir)
if glob.glob("*.m4a") != []:
    _m3u = open(sys.argv[1]+".m3u", "w")
    songlist = glob.glob("*.m4a")
    songlist.sort(key=os.path.getctime)
    for song in songlist:
        _m3u.write(song + "\n")
    _m3u.close()

os.chdir(curdir)
