import sys
from BeautifulSoup import BeautifulSoup
from datetime import datetime, date, time
import time
import jsonpickle

#Monday, November 3, 2014 at 3:17pm EST- expected input for raw_date_and_time (as a string)
def string_to_datetime(raw_date_and_time):
	list_raw = raw_date_and_time.split(" ")
	return datetime.strptime(list_raw[1][:3] + " " + list_raw[2][0:list_raw[2].index(",")] + " "  + list_raw[3] + " " + list_raw[5], '%b %d %Y %I:%M%p')

class Thread:
	def __init__(self, participants):
		self.participants = set(participants)
		self.messages = []

	def add_message(self, message):
		self.messages.append(message)

	def __str__(self):
		toReturn = ""
		list_part = list(self.participants)
		for idx in range(len(list_part)):
			if idx == len(list_part) - 1:
				toReturn += unicode(list_part[idx])
			else:
				toReturn += unicode(list_part[idx]) + ", "
		return toReturn

	def __repr__(self):
		return str(self.participants)

class Message:
	def __init__(self, user, text, raw_date_and_time):
		self.user = user.lstrip()
		self.text = text.replace("&#039;", "'").replace("&quot;", '"')
		self.date_and_time = string_to_datetime(raw_date_and_time)

	def __str__(self):
		return (self.user + " " + self.text + " " + str(self.date_and_time)).encode('utf-8')

	def __repr__(self):
		return (self.user + " " + self.text + " " + str(self.date_and_time)).encode('utf-8')

def main():
	start_time = time.time()
	f = open(sys.argv[1], 'r')
	html = f.read()
	output = open(sys.argv[2], 'w')
	print("Initializing data into the heap... (this could take a while)")
	soup = BeautifulSoup(html)
	dirty_threads = soup.findAll("div", { "class" : "thread" })
	clean_threads = []
	print("Parsing data begins...")
	for j in range(len(dirty_threads)):
		try:
			print("...Parsing thread " + str(j + 1) + " of " + str(len(dirty_threads)))
			dirty_thread = dirty_threads[j]
			string_participants = dirty_thread.contents[0].string
			participants = string_participants.split(",")
			for idx in range(len(participants)):
				participants[idx] = participants[idx].lstrip()
			clean_thread = Thread(participants)
			dirty_messages = (str(dirty_thread).split('<div class="message">'))
			for i in range(len(dirty_messages) - 1, 0, -1):
				if i != 0:
					bmessage = BeautifulSoup(dirty_messages[i])
					clean_message = bmessage.find("p").text
					clean_user = bmessage.find("span", { "class" : "user" }).text
					clean_date_time = bmessage.find("span", { "class" : "meta" }).text
					message = Message(clean_user, clean_message, clean_date_time)
					clean_thread.add_message(message)
			clean_threads.append(clean_thread)
		except AttributeError:
			print("...Thread " + str(j + 1) + " failed. Skipping...")
	print("Data parsing completed.")
	print("Finishing up...")
	og = (clean_threads)
	frozen = (jsonpickle.encode(og))
	output.write(frozen)
	output.close()
	print("Running time: %s seconds." % round(time.time() - start_time, 2))

if __name__ == "__main__":
	main()
