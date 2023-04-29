#!/bin/bash

videosPath="/home/acrodemocide/Videos"
backup="$videosPath/movie_backup"
movieDirectory="$videosPath/$1"

if [ -d "$backup" ]
then
	echo "backup file exists -- removing"
	rm -r "$backup"
fi

# We have the backup at the moment so that we can test that this script
# works without needing to go in and rip everything again
mkdir "$backup"
#cp -r $movieDirectory $backup

cd $movieDirectory
movieFile=$(ls -S | head -1)
echo "selected movie file: $movieFile"
find . ! -name "$movieFile" -type f -exec rm -f {} +
