import re
import datetime

def find_dates(read_filename, write_filename):
	'''write yyyy-mm-dd formate'''
	with open(read_filename, 'r') as read_file:
		with open(write_filename, 'w') as write_file:
			for line in read_file:
				match = re.search(r"(\d+)\t(.*)", line)
				id = match.group(1)
				text = match.group(2)
				text = norm_date(text)

				new_date = reg_date(text)
				pushed_40_date = new_date + datetime.timedelta(days=40)
				if new_date != 'N/A':
					# print(id + "\t" + new_date.strftime("%Y-%m-%d") + "\t" + pushed_40_date.strftime("%Y-%m-%d"))
					id_date_40date = id + "\t" + new_date.strftime("%Y-%m-%d") + "\t" + pushed_40_date.strftime("%Y-%m-%d") + "\n"
					write_file.write(id_date_40date)
			print("finished writing")

def norm_date(text):
	'''normaize the text month to number and formate as xx/xxxx or xx/xx/xxxx'''
	# 18 Jan 1990
	month_names = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05","Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
	regx1 = r"(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*(\d{4})"
	match1 = re.search(regx1, text)
	# June 25, 2012
	regx2 = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[., ]+(\d{1,2})[., ]+(\d{4})"
	match2 = re.search(regx2, text)
	# Jun 1987
	regx3 = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).*(\d{4})"
	match3 = re.search(regx3, text)

	if match1:
		text = re.sub(regx1, f"{month_names[match1.group(2)]}/{match1.group(1)}/{match1.group(3)}", text)

	elif match2:
		text = re.sub(regx2, f"{month_names[match2.group(1)]}/{match2.group(2)}/{match2.group(3)}", text)

	elif match3:
		text = re.sub(regx3, f"{month_names[match3.group(1)]}/{match3.group(2)}", text)

	return text

def reg_date(text):
	'''turn date str to datetime class'''
	# month, day, year xx/xx/xx AND xx/xx/xxxx
	match1 = re.search(r"(\d{1,2})(?:/|-)(\d{1,2})(?:/|-)(\d{4})", text)
	match2 = re.search(r"(\d{1,2})(?:/|-)(\d{1,2})(?:/|-)(\d{2})", text)

	# month and year
	match3 = re.search(r"(\d{1,2})/(\d{4})", text)

	# only year
	match4 = re.search(r"(\d{4})", text)

	if match1:
		new_date = datetime.datetime(int(match1.group(3)), int(match1.group(1)), int(match1.group(2)))

	elif match2:
		new_date = datetime.datetime(int('19' + match2.group(3)), int(match2.group(1)), int(match2.group(2)))

	elif match3:
		new_date = datetime.datetime(int(match3.group(2)), int(match3.group(1)), 1)

	elif match4:
		new_date = datetime.datetime(int(match4.group(1)), 1, 1)

	else:
		new_date = 'N/A'
	return new_date


if __name__ == '__main__':
	find_dates('./dates.txt', './LHS712-Assg1-qifanw.txt')
