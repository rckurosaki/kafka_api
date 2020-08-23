'''
This script is intended to simulate a api.
It reads a csv file and stream the data to Kafka.
'''

import csv
import time
import pickle

import kafka


def produce_raw_data(topic_name, csv_file_name):

	with open(csv_file_name) as file:
		csv_reader = csv.reader(file, delimiter=',')


		next(csv_reader) #skip the first row of the csv file

		counter = 1
		for row in csv_reader:
			item = pickle.dumps(row) #serialize the list to stream to kafka

		#send the data to kafka
			#.send(<topic>, <message>)
			_producer.send(topic_name, item)

			print('item ' + str(counter) + " inserted...")
			counter += 1

			time.sleep(0.02) #without the timeout the data is streamed instantly


if __name__ == '__main__':

	server_address = 'localhost:9092'
	topic_name = 'rawRamenList'
	csv_file_name = 'ramen-ratings.csv'


	_producer = kafka.KafkaProducer(bootstrap_servers=server_address)

	produce_raw_data(topic_name, csv_file_name)
