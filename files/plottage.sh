#!/bin/sh

(
echo ' set terminal pngcairo enhanced size 800,600 '
echo ' set encoding utf8 '
echo " set output \"$1.png\""
echo " set autoscale"
echo " set xdata time"
echo " set timefmt '%Y%m%d'"
echo " set grid"
echo " set xtics format '%d/%m'"
echo " set xlabel \"$(echo "$1" | sed -e "s/files\///")\""
echo " set title \"$(echo "$1" | sed -e "s/files\///")\" font \"Arial, 18\" textcolor rgb '#009C00'" 
echo " set style lines 1 lc rgb '#009C00' lw 3 pt 7 ps 1.3"
echo " plot \"$1\" using 2:1 title \"$(echo "$1" | sed -e "s/files\///")\" with linespoints ls 1 " ) > "$1".gnu

