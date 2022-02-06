import datetime

# from torch import ne
# date = '12/10/81'
# new_date = date.fromisoformat('2019-12-04')
# print(new_date)

x = datetime.datetime(2018, 9, 15)

print(x.strftime("%m-%d-%Y"))