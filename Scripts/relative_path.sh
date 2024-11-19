#!/bin/bash
 
full_path=$(realpath $0)
echo $full_path
 
dir_path=$(dirname $full_path)
echo $dir_path
 
#examples=$(dirname $dir_path )
#echo $examples
 
#data_dir="$examples/data"
#echo "DATA: $data_dir"
