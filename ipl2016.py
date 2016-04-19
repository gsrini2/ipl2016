from bs4 import BeautifulSoup
import urllib
from gi.repository import Notify
import time


url = 'http://www.cricbuzz.com/cricket-match/live-scores'

def printscore(scorediv):
	score = ""
	for runs in scorediv[0]:
		try:
			if runs.name == 'span':
				score+=runs.get_text()
			
			else:
				score += runs
		except:
			pass

	Notify.init("IPL T20")
	notification = Notify.Notification.new(score)
	notification.show()
	time.sleep(10)
	print score + "\n"
	Notify.uninit()
	notification.close()
	return

def ipl():
	while(True):
		request = urllib.urlopen(url).read()
		soup = BeautifulSoup(request)
		scorediv = soup.find_all("div", class_="cb-lv-scrs-col cb-font-12 text-black")
		printscore(scorediv)

def main():
    ipl()

if __name__ == "__main__":
    main()


	


	









