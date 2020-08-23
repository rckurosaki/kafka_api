'''
This script is responsable to consume the raw data from the kafka topic (rawRamenList),
process (cleaning) the data and to write the new data into the ramenList topic
'''

import pickle #to serialize and deserialize the data

from kafka import KafkaConsumer, KafkaProducer

#Cleaning the data consists in remove the 'Top Ten' column
#and make all attributes lowecase
def clean_data(topic_item):
	#the topic_item is a list with the attr: [Review ,Brand,Variety,Style,Country,Stars,Top Ten]
	topic_item.pop(-1) #to remove the last item of the list
	new_item = [x.lower() for x in topic_item]

	return new_item



def produce_clean_data(item):
	print(item)
	_producer.send(produce_topic, pickle.dumps(item)) #stream to the topic of clean data


if __name__ == '__main__':

	server_address = 'localhost:9092'

	consume_topic = 'rawRamenList'
	produce_topic = 'cleanRamenList'

	_consumer = KafkaConsumer(consume_topic, bootstrap_servers=server_address)
	_producer = KafkaProducer(bootstrap_servers=server_address)

	for consumer_item in _consumer:
		clean_item = clean_data(pickle.loads(consumer_item.value)) #clean the item

		produce_clean_data(clean_item)
		


