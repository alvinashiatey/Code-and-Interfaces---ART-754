#!/bin/bash
#This script will use jp2a to convert a jpg to ascii art

# first we check if jp2a is installed
if ! [ -x "$(command -v jp2a)" ]; then
  echo 'Error: jp2a is not installed.' >&2
  exit 1
fi

# define the output file and remove the extension
filename=$(basename -- "$1")
filename="${filename%.*}".txt

# if it is installed, we convert the image
jp2a --width=80  $1 > $filename

# we open the file
#open $filename

# loop through the txt file and print each line

#while read line; do
#  echo "$line"
#done < $filename

#loop through the txt file and create a new file with name from the line

while read line; do
  touch "$line"
done < $filename


# dont forget to make the script executable
# chmod +x script.sh
