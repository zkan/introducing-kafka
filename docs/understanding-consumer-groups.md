# Understanding Consumer Groups

Consumer แต่ละตัวจะอยู่ใน consumer group ถ้าเราไม่ได้กำหนด consumer group ให้ ทาง Kafka จะสร้าง group ขึ้นมาให้เอง ซึ่งใน 1 consumer group เราสามารถมี consumer ได้หลายตัว

## Working with Consumer Groups

เราจะใช้สคริป `kafka-consumer-groups.sh` ที่ Kafka มีให้เราในการทำความเข้าใจการทำงานของ consumer และ consumer group

### Listing Consumer Groups

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

### Describing consumer groups

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --all-groups
```

## Specifying Consumer Group for a Consumer

Consumer ที่ subscribe `my-first-topic` แบบไม่มี group เราจะใช้คำสั่งรัน consumer ขึ้นมาตามปกติ ซึ่งแบบนี้ Kafka จะสร้าง consumer group ขึ้นมาให้เอง

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-first-topic
```

Consumer ที่ subscribe `my-first-topic` แบบมี group ที่ชื่อว่า `my-first-group`

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-first-topic --group my-first-group
```

Consumer ที่ subscribe `my-first-topic` ที่อยู่ใน group `my-second-group` แบบดึง message จาก Kafka ตั้งแต่เริ่ม

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-first-topic --group my-second-group --from-beginning
```

