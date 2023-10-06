#!/bin/bash
echo "Youtube playlist downloader started" 
cd /home/sricharan/Desktop/'youtube playlist downloader'
var=$(pwd)
echo "The current working directory $var."
python3 urls.py
echo "Started downloading"
python3 downloadyt.py
echo "Successfully playlist downloaded :)"
