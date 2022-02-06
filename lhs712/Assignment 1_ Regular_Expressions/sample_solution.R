file_path = "./dates.txt"
output_file_path = "./output.txt"
sink(output_file_path)

data = read.table(file_path, header = F, sep = '\t', stringsAsFactors=FALSE, quote = "")

# You could define month names as a data frame and use it to normalize, using month_names[month][1,1]
month_names <- data.frame(
  Jan = '01', Feb = '02', Mar = '03', Apr = '04',May = '05',Jun = '06',
  Jul = '07', Aug = '08' , Sep = '09', Oct = '10', Nov = '11', Dec = '12'
)

# Example of how to write a function. This function matches a given pattern in a given line
find_pattern<-function(pattern,line){
  return (regmatches(line, regexpr(pattern, line)));
}

# Example of a pattern finding function
find_pattern_1<-function(line,id){
  pattern = '\\d'
  pattern = "?:\\d{2}"
  pattern = "\\d{1,2}"
  s = find_pattern(pattern, line)
  if(length(s) > 0){
	# Work with the matched section s
    cat(id, "\t", s, "\n", sep="")
    return (TRUE)
  }
  return (FALSE)
}

for(i in 1:500){
  line = data[i,2]
  
  find_pattern_1(line,i)
  # if find_pattern_1 returns FALSE, find another pattern, and so on...
}
sink()

