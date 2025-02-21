# Producing Messages to Kafka

Producer แบบไม่ได้กำหนด key

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic odds
```

Producer แบบมี key

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic odds --property "parse.key=true" --property "key.separator=:"
```