import sys
from datetime import datetime, date, time
import time
import jsonpickle
from convert import Thread, Message

def thread_counter(thread_to_analyze, verbose=True, print_user=False, user=None):
	participant_dict = {}
	for participant in thread_to_analyze.participants:
		participant_dict[participant] = 0
	for message in thread_to_analyze.messages:
		try:
			participant_dict[message.user] += 1
			if print_user and user == message.user:
				print(message.text)
		except KeyError:
			if message.user + "(Removed or Left Conversation)" in participant_dict:
				participant_dict[message.user + "(Removed or Left Conversation)"] += 1
			else:
				participant_dict[message.user + "(Removed or Left Conversation)"] = 1
	if verbose:
		for participant in participant_dict:
			print('User: {}, Messages Sent: {}'.format(unicode(participant), participant_dict[participant]))

	return participant_dict

def main():
	print("Loading...(this could take a few minutes)")
	f = open(sys.argv[1], 'r')
	threads = jsonpickle.decode(f.read())
	choice = 0
	while choice != 4:
		choice = int(input("1) Analyze Thread\n2) Analyze User (output user's messages to a file)\n3) Analyze Set of Users\n4) Quit\nInput: "))
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
			thread_counter(thread_to_analyze)
			print("\n")
		elif choice == 2:
			pass
		elif choice == 3:
			input_string = raw_input("Enter a list of users separated by commas with no spaces between one name and the next (ex: Bob Smith,John Doe,Jane Doe): \n")
			specific_user_string = raw_input("Do you want the messages of a specific user? (y/n,FirstName LastName)")
			input_set = set(input_string.split(","))
			name = None
			if specific_user_string[0] == "y":
				specific_user_set = specific_user_set.split(",")
				name = specific_user_set[1]
			input_dictionary = {}
			for participant in input_set:
				input_dictionary[participant] = 0
			for thread in threads:
				if thread.participants >= input_set:
					temp_dict = {}
					if name is not None:
						temp_dict = thread_counter(thread, False, True, name)
					else:
						temp_dict = thread_counter(thread, False)
					for participant in input_dictionary:
						input_dictionary[participant] += temp_dict[participant]
			for participant in input_dictionary:
				print('User: {}, Messages Sent: {}'.format(unicode(participant), input_dictionary[participant]))
		# user_to_analyze = raw_input("User to analyze: ")
		# for message in thread_to_analyze.messages:
		# 	if message.user == user_to_analyze:
		# 		try:
		# 			print(message.text)
		# 		except UnicodeEncodeError:
		# 			print('An error occurred with this thread. Skipping...')

if __name__ == "__main__":
	main()
