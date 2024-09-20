puts "enter length"
length = gets.chomp
puts "enter width"
width = gets.chomp
length = length.to_f
width = width.to_f
area = length * width
perim = 2 * length + 2 * width
perim = perim.to_s
area= area.to_s
puts "the are is " + area
puts "the perim is " + perim 
/*
enter length
2
enter width
2
the are is 4.0
the perim is 8.0
*/