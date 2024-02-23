# How to run the code


## Run the kafka server
Make sure you run your kafka application, zookeeper etc

Open kafka directory and run the following:

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Open another terminal and inside the kafka directory 

```
bin/kafka-server-start.sh config/server.properties
```

Next create topics and other configurations

```
bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```


## Run the code 
Now clone the repository.

```
git clone https://github.com/asifrahaman13/sample-kafka-sdk
```

Create a virtual environment.

```
virtualenv .venv
```

Activate the virtual environment

```
source ./venv/bin/activate
```

Next you can install the dependencies and packages. 

```
pip install -r requirements.txt
```


Note that the package example_package_asifr_berhampore is already included. 

Next run the sample server. 

```
uvicorn main:app --reload 
```

Open another terminal to check the output from the kafka consumer.

```
python3 consumer.py
```

## Sample screenshot:


![alt text](<Screenshot from 2024-02-23 18-27-25.png>)