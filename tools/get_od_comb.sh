#!/bin/bash
# Filtramos todas las posibles combinaciones origen-destino. 

# Definimos algunas variables. Ojo que a bash no le gustan los espacios cerca del "=".
year="2008"
infile="../data/2008.csv"
outfile="od_comb_2008.csv"

tail -n +2 $infile | cut -f17,18 -d, | sort | uniq > $outfile
