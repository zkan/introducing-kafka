# Kafka Partitioning

## How Partitioning Works

Kafka แบ่ง topic ออกเป็น partitions ถ้า message ที่ส่งเข้ามาไม่มี key แนบมาด้วย message จะถูกกระจายไปตาม partitions ของ topic นั้น ๆ (partition assignment) แบบ round-robin ดังนั้นถ้าเป็นการกระจาย message ไปตาม partitions แล้ว เรื่อง order จะไม่ถูก guarantee

ถ้า message มี key แนบมาด้วย จะทำให้ partition จะถูกเลือกจาก hash ของ key ที่ส่งเข้ามา แล้ว modulus ด้วยจำนวน partitions ถ้าเป็นแบบนี้แล้ว Kafka ก็จะ guarantee ว่า message ที่เข้ามาด้วย key เดียวกัน จะไปลง partition เดียวกัน ดังนั้นเรื่อง order ก็จะ guarantee ด้วยเช่นกัน

ยกตัวอย่างการใช้ key เช่น เราอาจจะกำหนด key ที่ใช้เป็น customer ID ถ้าเราต้องการดู activity หรือ event ที่เข้ามาจาก customer คนนั้น ๆ เราจะได้ event ที่มี order ที่ guarantee

## Producing Messages *without* Key

สร้าง topic ใหม่ที่มีชื่อว่า `my-topic-with-partitions` ที่มี 2 partitions หรือมากกว่า

```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my-topic-with-partitions --partitions 2
```

รัน producer แบบไม่ได้กำหนด key ให้ส่ง message เข้าไปที่ topic `my-topic-with-partitions`

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic my-topic-with-partitions
```

รัน consumer ขึ้นมา 2 ตัวให้อยู่ใน group เดียวกันที่ชื่อว่า `without-key`

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic-with-partitions --group without-key
```

!!! note

    สาเหตุที่รัน consumer ขึ้นมา 2 ตัว เป็นเพราะว่าเรามี 2 partitions เราจะได้เห็นการ distribute messages ไปยัง partition ต่าง ๆ ที่ consumer รออ่าน message อยู่

เสร็จแล้วให้ลองส่ง message จาก producer เข้าไปเรื่อย ๆ แล้วดูผลลัพธ์

## Producing Messages *with* Key

เราจะใช้ topic เดิมจากหัวข้อที่แล้วที่ชื่อว่า `my-topic-with-partitions` แล้วรัน consumer ขึ้นมาใหม่อีก 2 ตัวให้อยู่ใน group เดียวกันที่ชื่อว่า `with-key`

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic-with-partitions --group with-key
```

เสร็จแล้วให้รัน producer แบบมี key ด้วยคำสั่งตามนี้

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic my-topic-with-partitions --property "parse.key=true" --property "key.separator=:"
```

เวลาที่เราจะส่ง message เราต้องพิมพ์ message ที่มีการแบ่ง key กับ message ด้วย `:` เช่น `1:hello` จะหมายความว่า key คือ `1` และ message คือ `hello`

เสร็จแล้วให้ลองส่ง message แบบมี key จาก producer เข้าไปเรื่อย ๆ แล้วดูผลลัพธ์
