from example_package_asifr_berhampore.example_package_asifr_berhampore import TrafficProcessingSDK

kafka_bootstrap_servers = 'localhost:9092'
group_id="traffic-processing-group"
sdk = TrafficProcessingSDK(kafka_bootstrap_servers, group_id)

sdk.consume_from_kafka()