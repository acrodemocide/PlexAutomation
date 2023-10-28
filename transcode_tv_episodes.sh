#!/bin/bash

for file in ./*;
do
	if [[ "$file" == *.mkv ]]
	then
		basename=$(basename "$file")
		name="${basename%.mkv}"
#		HandBrakeCLI -i "$file" -o "~/Videos/$name.mp4" --all-subtitles --format "av_mp4" --optimize
		HandBrakeCLI -i "$file" -o "$name.mp4" --all-subtitles --format "av_mp4" --optimize
#		echo "~/Videos/$name.mp4"
	fi
done

