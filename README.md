# mp4cat
Concatenate MP4 files in natural numerical order to one single file and add an audio file

git clone https://github.com/jamdoran/mp4cat

add alias to .zshrc
alias mp4cat='cd ~/Documents/Git/mp4cat && source .venv/bin/activate && python mp4cat.py'

ffmpeg required
python 3.10 required

Mac Only, but probably works on Linux

-> Audio file must be called music.mp4
-> Other files must be numerically ordered  file1.mp4, file2.mp4 etc.
-> Sort order is natural file1, file2 etc not file1, file10

Required ffmpeg to be installed via brew

