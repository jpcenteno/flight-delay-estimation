#!/bin/bash

if [ $# -ne 1 ]; then echo "Se necesita el año" ; exit 1; fi

year=$1

for link in $(grep ${year}.csv dataset_list.txt)
do
    wget -c $link
    mv *.csv ../data/
    mv *.bz2 ../data/
done

