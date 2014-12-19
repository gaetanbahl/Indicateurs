 set terminal pngcairo enhanced size 800,600 
 set encoding utf8 
 set output "Documents relus.png"
 set autoscale
 set xdata time
 set timefmt '%Y%m%d'
 set grid
 set xtics format '%d/%m'
 set xlabel "Documents relus"
 set title "Documents relus" font "Arial, 18" textcolor rgb '#009C00'
 set style lines 1 lc rgb '#009C00' lw 3 pt 7 ps 1.3
 plot "files/Documents relus" using 2:1 title "Documents relus" with linespoints ls 1 
