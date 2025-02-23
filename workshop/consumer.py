# import json

from confluent_kafka import Consumer


topics = ["my-topic-with-partitions",]

c = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "without-key",
    "auto.offset.reset": "earliest",
})
c.subscribe(topics)

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue

    data = msg.value().decode("utf-8")
    print(data)

    # data = json.loads(msg.value().decode("utf-8"))
    # print(data["text"])

c.close()