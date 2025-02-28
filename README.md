This will be a distributed ETL pipeline for real-time financial data processing using Kafka and Spark Streaming. Extracted stock price data from an API, processed it in a distributed system, and stored structured data in PostgreSQL for financial analytics.

Goal
- Extract stock market data from an API
- Transform it into a structured format
- Load it into a database while streaming data in real-time
- Use Kafka as the event-driven system for distributed data processing

Tech stack:
Component	        Technology
Message Broker	    Kafka (Producer/Consumer)
Data Processing	    Python (pandas, requests)
Database	        PostgreSQL (or SQLite for local testing)
Distributed         Computing	Apache Spark (later enhancement)

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

Ctrl + C to exit shells

Set up Kafka Producer
Install dependencies: pip install requests kafka-python pandas psycopg2-binary

Set up Consumer
pip install kafka-python psycopg2-binary
kafka-python -> Enables Python to consume messages from Kafka
psycopg2-binary -> Allows Python to interact with PostgreSQL 
python-dotenv --> to hide API key


Notes on Kafka:
- Previously had Kafka-related directories, but not full Kafka install (i.e. no kafka-server-start.sh or kafka-topics.sh)
- Kafka-related Python packages (confluent_kafka) - likely from a Python library (confluent-kafka), but not full Kafka server
- Projects did not have the Kafka broker

Determine if Kafka and Zookeeper are running
- brew services list
to restart postgres: 
- brew services restart postgresql@14
to manually start postgres: 
- pg_ctl -D /opt/homebrew/var/postgresql@14 start
check versions of postgres:
- brew list | grep postgresql
which version running:
- pg_ctl -D /opt/homebrew/var/postgresql@14 status
upgrade shell to use homebrew postgres 14:
- ls /opt/homebrew/bin/psql
prioritize postgres 14:
- echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
- source ~/.zshrc
verify version
- psql --version
start postgres14:
- pg_ctl -D /opt/homebrew/var/postgresql@14 start
Check if postgres is running on 5432:
- lsof -i :5432
Kill the running postgres process:
- kill -9 1804
Stop postgres via homebrew:
- brew services stop postgresql@14
restart postgres:
- pg_ctl -D /opt/homebrew/var/postgresql@14 start
is postgres fully operational?
- pg_ctl -D /opt/homebrew/var/postgresql@14 status
Connect to psql:
- psql -d postgres
If needed run psql in the background:
- brew services start postgresql@14


Adding Spark
- brew install apache-spark
Verify:
- spark-submit --version
Verify pyspark:
- pyspark --version
Enter spark shell:
- pyspark
Test:
- spark.range(10).show()
Exit:
- exit()
Install dependencies:
- pip install pyspark findspark
