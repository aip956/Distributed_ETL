

Install
brew --version ()
brew update --force
brew upgrade
brew install kafka

List Kafka topics:
kafka-topics.sh --list --bootstrap-server localhost:9092
bash: kafka-topics.sh: command not found

Add Kafka to my path
echo 'export PATH="/opt/homebrew/opt/kafka/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

Start zookeeper
 brew services start zookeeper

Start Kafka
rew services start kafka

List topics: (None yet)
kafka-topics --list --bootstrap-server localhost:9092

(venv) MacBookPro:distrETL antheaip$ 

Create test topic
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Start Kafka producer:
kafka-console-producer --broker-list localhost:9092 --topic test-topic

Start kafka consumer in new terminal:
kafka-console-consumer --bootstrap-server localhost:9092 --topic test-topic --from-beginning
(will show what i typed in the producer)


