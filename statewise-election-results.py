import requests
import time
import bs4
import lxml

pennl=0
georgial=0

while(True):
	georgia=requests.get("https://www.foxnews.com/elections/2020/general-results/state/georgia")
	soup = bs4.BeautifulSoup(georgia.text, 'lxml')
	georgia = soup.find_all(class_="votes")
	georgiab=int(georgia[0].text.replace(',', ''))
	georgiat=int(georgia[1].text.replace(',', ''))
	if(georgiat-georgiab<georgial):
		print("Georgia : ")
		change=abs(georgial-(georgiat-georgiab))
		georgial=georgiat-georgiab
		print("Lead : ", georgial, "Decreased by ", change)
		print("\n")
	if(georgiat-georgiab>georgial):
		print("Georgia : ")
		change=abs(georgial-(georgiat-georgiab))
		georgial=georgiat-georgiab
		print("Lead : ", georgial, "Increased by ", change)
		print("\n")

	penn=requests.get("https://www.foxnews.com/elections/2020/general-results/state/pennsylvania")
	soup = bs4.BeautifulSoup(penn.text, 'lxml')
	penn = soup.find_all(class_="votes")
	pennb=int(penn[0].text.replace(',', ''))
	pennt=int(penn[1].text.replace(',', ''))
	if(pennt-pennb<pennl):
		print("Pennsylvania : ")
		change=abs(pennl-(pennt-pennb))
		pennl=pennt-pennb
		print("Lead : ", pennl, "Decreased by ", change)
		print("\n")
	if(pennt-pennb>pennl):
		print("Pennsylvania : ")
		change=abs(pennl-(pennt-pennb))
		pennl=pennt-pennb
		print("Lead : ", pennl, "Increased by ", change)
		print("\n")

	time.sleep(5)