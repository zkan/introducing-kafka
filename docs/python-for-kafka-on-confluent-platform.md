# Python for Kafka (on Confluent Platform)

ในเวิร์คชอปนี้เราจะใช้ Confluent Platform ในการรัน Kafka และ schema registry
และโค้ดที่ใช้ในเวิร์คชอปนี้จะอยู่ที่โฟลเดอร์ `workshop/` ดังนั้นให้เราเข้าไปที่โฟลเดอร์นั้นก่อน

## Starting the Confluent Platform

```bash
docker compose up
```

## Running a Producer

```bash
python json_producer.py -b localhost:9092 -s http://localhost:8081 -t topic_52
```

## Running a Consumer

```bash
python json_consumer.py -b localhost:9092 -s http://localhost:8081 -t topic_52 -g my-group
```
