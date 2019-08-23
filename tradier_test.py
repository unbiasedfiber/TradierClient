from Tradier import TradierClient
import csv

t = TradierClient('KEY', True)
res = t.get_quote_history("APHA", "daily", "2019-06-01", "2019-08-23")
data = res["history"]["day"]


with open("./apha_quotes.csv", "w", newline="") as csvfile:
    myfile = csv.writer(csvfile, delimiter=',')
    myfile.writerow(data[0].keys())
    for day in data: myfile.writerow(day.values())
