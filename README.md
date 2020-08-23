### kafka_api
Simple project to learn more in depth Apache Kafka and how to produce and consume events.

Data used in this project can be found [here](https://www.kaggle.com/residentmario/ramen-ratings?select=ramen-ratings.csv).

Useful commands to kafka:
* Create topic: bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic <topic_name>
* List the topics: bin/kafka-topics.sh --list --zookeeper localhost:2181
* Remove topic: bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic <topic_name>

##### What this does?
The project contains a csv file, a api_simulator and a consumer. 
The api_simulator will read the csv file and produce events to one topic in the kafka server. This is a simulation to a real time api witch keeps getting new data.
Then, the consumer will get the raw data from the topic, do some cleaning of this data and finally produce new events to a new topic.
