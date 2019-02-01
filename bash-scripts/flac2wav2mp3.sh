#! /bin/bash


checkargs () {
if [[ $OPTARG == ^-* ]]
then
    echo "Probably bad argument for option!"
    exit 1
fi
}


if [ -z $* ] && [ ! -e "$1" ]
then
	echo "No DIR given!"
	echo "Usage:"
	echo "$0 SRC_DIR [-s IF_TO_BE_SPLITTED] [-f TRGT_FORMAT]"
	exit 1
fi


while getopts "hs:f:" opt
do
	case $opt in
		h) checkargs
		   echo "$0 [-h] [-s BOOL] -f FORMAT SOURCE_DIR" # is the order of source_dir correct here?
		   echo "[-h] for help"
		   echo "[-s] means split, values: yes or no"
		   echo "[-f] means target format, values: flac or mp3"
		   exit 0
		   ;;
	   	s) checkargs
	   	   SPLIT="$OPTARG"
		   ;;
	   	f) checkargs
	   	   TRGT_FORMAT="$OPTARG"
		   ;;
	   	*) echo "No reasonable options found!"
		   ;;
	esac
done
shift $((OPTIND-1))


SRC_DIR="$(realpath "$*")"                # Need to add parsing several dirs.
TRGT_DIR="$SRC_DIR"_"$TRGT_FORMAT"
mkdir "$TRGT_DIR"


findCUE ()
# echoes the abspath of the first found *.cue
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


CUE=`findCUE "$SRC_DIR"`
if [ -z "$CUE" ] || [ -z "$SPLIT" ]
then $SPLIT=no
fi


split2fmt ()
{
	if [[ "$TRGT_FORMAT" == mp3 ]]
	then
		shnsplit -f "$CUE" -t "%n %t" -o 'cust ext=mp3 lame --preset insane -q 0 - %f' `ls | grep -E "$SRC_DIR/*.ape|$SRC_DIR/*.flac"` -d "$TRGT_DIR"
    elif [[ "$TRGT_FORMAT" == flac ]]
    then
        shnsplit -f "$CUE" -t "%n %t" -o "flac ext=flac flac -s -8 -o %f -" `ls | grep -E "$SRC_DIR/*.ape|$SRC_DIR/*.flac"` -d "$TRGT_DIR"
    else
        echo -e "Bad argument for '-t' option:\n
                 mp3 or flac expected, but got "$TRGT_FORMAT""
        exit 1
    fi
}


encode ()
{
    if [[ "$TRGT_FORMAT" == mp3 ]]
	then
        #here starts for-loop?
        for f in "$SRC_DIR"/"*.{flac,ape,wav,wv,m4a,wma,aif,aiff}" # ??
        do
		    lame --preset insane -q 0 `ls | grep -E "$SRC_DIR/*.ape|$SRC_DIR/*.flac"` # where to save -d "$TRGT_DIR"
		done  #may be here something like:  <  ?
		# or maybe look at:
		# https://unix.stackexchange.com/questions/428018/how-to-convert-all-wav-files-in-subdirectories-to-flac

    elif [[ "$TRGT_FORMAT" == flac ]]
    then
        cd "$SRC_DIR"
        flac -s -8 --output-prefix="$TRGT_DIR"/ *.{ape,wav,wv,m4a,wma,aif,aiff} # should interact like: files of which format to encode?
    else
        echo -e "Bad argument for '-t' option:\n
                 mp3 or flac expected, but got "$TRGT_FORMAT""
        exit 1
    fi
}


if [[ $SPLIT == yes ]]
then
    split2fmt
elif [[ $SPLIT == no ]]
then
    encode
else
    echo "Bad argument for option -s"
    exit 1
fi



#MP3_DIR=../`echo $PWD | gawk 'match($0, /.*\/(.*)$/, a) {print a[1]}'`_mp3

	#shnsplit -f "$CUE" -t "%n %t" -o flac *."$WHAT" -d "$SDF"
	#`ls | grep -E "*.ape|*.flac"


#for f in "$SRC_DIR"/*.flac
#do
#		flac -d "$f"
#       WAV_F=`echo "$f" | sed s/\.flac$/.wav/g`
#		lame --preset insane "$WAV_F"
#		rm -v "$WAV_F"
#		MP3_F=`echo "$f" | sed s/\.flac$/.mp3/g`
#		mv -v "$MP3_F" "$MP3_DIR"
#done