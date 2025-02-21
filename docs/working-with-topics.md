# Working with Topics

คำสั่ง list topics

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

เปลี่ยนจาก `localhost` เป็น Public IP ของเครื่องนั้นๆ

```bash
bin/kafka-topics.sh --bootstrap-server 13.212.73.116:9092 --list
```

สร้าง topic ชื่อ odds

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic odds
```

ลบ topic

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic odds
```

สร้าง topic ชื่อ odds แบบมี 3 partitions

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic odds --partitions 3
```

คำสั่ง describe topics

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe
```

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic odds
```