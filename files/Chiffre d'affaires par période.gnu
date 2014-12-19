 set terminal pngcairo enhanced size 800,600 
 set encoding utf8 
 set output "Chiffre d'affaires par période.png"
 set autoscale
 set xdata time
 set timefmt '%Y%m%d'
 set grid
 set xtics format '%d/%m'
 set xlabel "files/Chiffre d'affaires par période"
 set title "Chiffre d'affaires par période" font "Arial, 18" textcolor rgb '#009C00'
 set style lines 1 lc rgb '#009C00' lw 3 pt 7 ps 1.3
 plot "files/Chiffre d'affaires par période" using 2:1 title "Chiffre d'affaires par période" with linespoints ls 1 
