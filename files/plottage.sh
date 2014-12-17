#!/usr/bin/sh

( echo " set terminal jpg color enhanced "Helvetica" 20"
echo " set output 'graph.tex'"
echo " set autoscale"
echo " set xtics auto"
echo "set ylabel "\\rotatebox{90}{Temps de compression (s)}""
echo "set xlabel $1  "

echo " plot '$1' using 1:2 notitle with lines" " ) > "$1"
