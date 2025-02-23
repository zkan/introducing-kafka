from confluent_kafka import Producer


topic = "my-topic-with-partitions"

p = Producer({
    "bootstrap.servers": "localhost:9092"
})

p.produce(topic, "Hello")
p.flush()
