import sys
from datetime import datetime, date, time
import time
import jsonpickle
from convert import Thread, Message

def main():
	print("Loading...(this could take a few minutes)")
	f = open(sys.argv[1], 'r')
	threads = jsonpickle.decode(f.read())
	choice = 0
	while choice != 3:
		choice = int(input("1) Analyze Thread\n2) Analyze User\n3) Quit\nInput: "))
		if choice == 1:
			print("List of Threads: ")
			for idx in range(len(threads)):
				try:
					print('{}) {}'.format(idx, threads[idx]))
				except UnicodeEncodeError:
					print('An error occurred with this thread. Skipping...')
			try:
				index = int(input("\nThread to analyze: "))
				if index >= len(threads) or index < 0:
					raise NameError()
			except NameError:
				print("Invalid input.")
				sys.exit(-1)
			thread_to_analyze = threads[index]
			participant_dict = {}
			for participant in thread_to_analyze.participants:
				participant_dict[participant] = 0
			for message in thread_to_analyze.messages:
				try:
					participant_dict[message.user] += 1
				except KeyError:
					if message.user + "(Removed or Left Conversation)" in participant_dict:
						participant_dict[message.user + "(Removed or Left Conversation)"] += 1
					else:
						participant_dict[message.user + "(Removed or Left Conversation)"] = 1
			for participant in participant_dict:
				print('User: {}, Messages Sent: {}'.format(unicode(participant), participant_dict[participant]))
			print("\n")
		# user_to_analyze = raw_input("User to analyze: ")
		# for message in thread_to_analyze.messages:
		# 	if message.user == user_to_analyze:
		# 		try:
		# 			print(message.text)
		# 		except UnicodeEncodeError:
		# 			print('An error occurred with this thread. Skipping...')

if __name__ == "__main__":
	main()
