import re
import datetime


new_date = datetime.datetime(2000, 1, 1)
pushed_40_date = new_date + datetime.timedelta(days=40)
print(pushed_40_date.strftime("%Y-%m-%d"))
# month_names = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05","Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
# text = 'Jun 1987blaaaaa'
# regx1 = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*(\d{4})"
# match1 = re.search(regx1, text)
# if match1:
# 	text = re.sub(regx1, f"{month_names[match1.group(1)]}/{match1.group(2)}", text)

# print(text)
# def find_dates(filename):
# # You could define the following to normalize months, using month_names[month]
# 	month_names = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05","Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

# 	with open(filename, 'r') as file:
# 		for line in file:
# 			match = re.search(r"(\d+)\t(.*)", line)
# 			id = match.group(1)
# 			text = match.group(2)

# 			# Search regular expressions in text. For example, the line below searches for a digit
# 			match = re.search(r"(May|Feb)", text)
# 			if match:
# 				# work with what matched. match.group(0) is everthing that matched the regex. If you used () in your regex, match.group(1) represents the first (), and so on...
# 				print (id + "\t" + match.group(0)) ;
# # Jan 1987
# # Marc, 1981
# # June, 1999
# # January 2007

# # June 25, 2012
# # September. 15, 2011
# # 18 Jan 1990
# (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*(\d{4})


# if __name__ == '__main__':
# 	find_dates('./dates.txt')
