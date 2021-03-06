import urllib2, csv
from bs4 import BeautifulSoup

output_file = open ("deathrow.csv", "w")
writer = csv.writer(output_file)

url = "https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"

html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser") 

table = soup.find("table", {"class": "tdcj_table indent"})

for tr in table.find_all("tr"):

		td_list = tr.find_all("td")

		data = [cell.text for cell in cell_list]

		writer.writerow(data)