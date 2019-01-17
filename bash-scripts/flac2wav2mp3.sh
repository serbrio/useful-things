#! /bin/bash

if [ -z $* ]
then 
	echo "No DIR given!"
	exit 1
fi

findCUE ()
{
	local WHERE="$1"
	for f in "$WHERE"/*
       	do
		if [[ "$f" == *\.cue ]]
		then 
			local CUE="$(realpath "$f")"
			echo "$CUE"
			break
		fi
	done
}

ape_flac2flacs ()
{
	local WHAT="$1"
	local WHERE="$(realpath "$2")"
	local SDF="$SD"_FLACS
	mkdir "$SDF"
	local CUE=`findCUE $SD` 
	
	if [[ "$TOWHAT" == mp3 ]]
	then 
		shnsplit -f "$CUE" -t "%n %t" -o 'cust ext=mp3 lame --preset insane -q 0 - %f' *."$WHAT" -d

	shnsplit -f "$CUE" -t "%n %t" -o flac *."$WHAT" -d "$SDF"
	#`ls | grep -E "*.ape|*.flac"

}



while getopts "hfam" opt
do
	case $opt in
		h) echo "$0 [-hfam] SOURCE_DIR"
		   echo "-h for help"
		   echo "-f splits FLAC according to the first found in source dir CUE file;
		            results saved in SOURCE_DIR__FLACS"
		   echo "-a splits APE to FLAC according to the first found in SOURCE_DIR CUE file;
		            results saved in SOURCE_DIR__FLACS"
		   echo "-m converts all FLACs found in SOURCE_DIR 
		            (SOURCE_DIR__FLACS, if -s or -a specified) to MP3;
			    results saved in SOURCE_DIR__MP3"
		   exit 0
		   ;;
	   	f)
			shift;;
	   	a)
			shift;;
	   	m)
			shift;;

	esac
done


echo "SRC [splitflac ape]"
SRC_DIR=$1
#MP3_DIR=../`echo $PWD | gawk 'match($0, /.*\/(.*)$/, a) {print a[1]}'`_mp3
MP3_DIR="$SRC_DIR"_mp3
mkdir "$MP3_DIR"

if splitflac (means split flac)
then shnsplit -f cue -t "%n %t" -o flac


       	
if ape

for f in "$SRC_DIR"/*.flac
do
		flac -d "$f"	
        WAV_F=`echo "$f" | sed s/\.flac$/.wav/g`
		lame --preset insane "$WAV_F"
		rm -v "$WAV_F"
		MP3_F=`echo "$f" | sed s/\.flac$/.mp3/g`
		mv -v "$MP3_F" "$MP3_DIR" 
done


func () 
{

}


for d in KOVAL/*/*; do if [[ "$d" == *\.cue ]]; then echo $d; fi; done
shnsplit -f cue.cue -t "%n %t" -o flac Pieter.ape
