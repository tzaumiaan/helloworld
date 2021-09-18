#target="comforting_sounds_20200229"
#listcode="PLXn-CwyOz08W25HGnxxazPIxsFvYRS6aV"
target="funk_20200229"
listcode="PLXn-CwyOz08X0b6KCKnwxFu4NjTW8woNz"
mkdir -p ${target}
cd ${target}
youtube-dl --extract-audio --audio-format m4a -o "%(title)s.%(ext)s" ${listcode}
cd ..
python plgen.py ${target}
