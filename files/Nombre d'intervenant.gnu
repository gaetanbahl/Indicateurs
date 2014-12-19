 set terminal png enhanced size 800,600 
 set encoding utf8 
 set output "Nombre d'intervenant.png"
 set autoscale
 set xdata time
 set timefmt '%Y%m%d'
 set grid
 set xtics format '%d/%m'
 set xlabel "files/Nombre d'intervenant"
 set title "Nombre d'intervenant" font "Arial, 18" textcolor rgb '#009C00'
 set style lines 1 lc rgb '#009C00' lw 3 pt 7 ps 1.3
 plot "files/Nombre d'intervenant" using 2:1 title "Nombre d'intervenant" with linespoints ls 1 
