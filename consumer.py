# Import my sample package for kafka
from example_package_asifr_berhampore.example_package_asifr_berhampore import (
    TrafficProcessingSDK,
)

# Set the initial configurations for the kafka consumer.
kafka_bootstrap_servers = "localhost:9092"
group_id = "traffic-processing-group"

# Create an instance of the TrafficProcessingSDK class and consume from kafka.
sdk = TrafficProcessingSDK(kafka_bootstrap_servers, group_id)

# Call the consume_from_kafka method to consume from kafka.
sdk.consume_from_kafka()
