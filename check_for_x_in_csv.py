import csv

with open('is_reward_sent.csv', 'r') as csv_file: 
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	count = 0

	with open('rewards_unsent_emails.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file)

		for line in csv_reader:
			if line[1] != 'X':
				count += 1
				csv_writer.writerow([line[0]])

		print(count, "emails have not received rewards.")