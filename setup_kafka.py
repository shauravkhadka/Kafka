from kafka.admin import KafkaAdminClient, NewTopic

def create_topic(topic_name, num_partitions, replication_factor):
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092",
        client_id='test_admin'
    )

    topic_list = []
    topic_list.append(NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

create_topic("test2", 3, 1)
