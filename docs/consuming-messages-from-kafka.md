# Consuming Messages from Kafka

Consumer ที่ subscribe odds แบบไม่มี group

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic odds
```

Consumer ที่ subscribe odds แบบมี group

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic odds --group dc
```

Consumer ที่ subscribe odds แบบดึง message จาก broker ตั้งแต่เริ่ม

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic odds --group mygroup --from-beginning
```

## Listing Consumer Groups

List consumer groups

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

Describe consumer groups

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --all-groups
```