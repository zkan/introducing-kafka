# Python for Kafka with Schema Registry (on Confluent Platform)

ในเวิร์คชอปนี้เราจะใช้ Confluent platform ในการรัน Kafka ซึ่งใน platform นี้จะมี feature
และ component ต่าง ๆ ให้เราสามารถเรียนรู้ Kafka ได้สะดวกมากขึ้น ซึ่ง component
หนึ่งที่เราหยิบมาใช้งานในเวิร์คชอปนี้คือ [schema
registry](https://docs.confluent.io/platform/current/schema-registry/index.html){target=_blank}

## Why Schema Registry?

ใน Kafka เราสามารถกำหนดโครงสร้างรูปแบบของข้อมูลในการรับส่งได้ โดยผ่านการกำหนด *schema*
ในการรับส่ง message ร่วมกัน ซึ่งการกำหนดนั้นเราสามารถกำหนดโดยใช้รูปแบบข้อมูล Avro, JSON หรือ
Protobuf ได้ โดยที่ schemas ต่าง ๆ ควรจะถูกจัดเก็บใน component ที่เราเรียกกันว่า schema
registry

Schema registry คือ centralized repository สำหรับการจัดการ
และการตรวจสอบความถูกต้องของ schemas สำหรับ message ต่าง ๆ และสำหรับการทำ
serialization และ deserialization ของข้อมูล ทั้ง producers และ consumers สามารถใช้
schemas เพื่อทำให้มั่นใจว่าข้อมูลที่รับส่งกันมีเรื่อง consistency และ compatibility ด้วย
อีกทั้งยังช่วยเรื่อง data governance และ data quality ในองค์กรด้วยเช่นกัน

## Starting the Confluent Platform

โค้ดที่ใช้ในเวิร์คชอปนี้จะอยู่ที่โฟลเดอร์ `workshop/` ดังนั้นให้เราเข้าไปที่โฟลเดอร์นี้ก่อน

รัน Confluent platform ขึ้นมาโดยใช้คำสั่ง

```bash
docker compose up
```

หลังจากรันคำสั่งข้างบนแล้ว เราจะสามารถเข้า Control center ที่เป็นหน้า UI ของ Confluent
platform ได้ที่ [http://localhost:9021/](http://localhost:9021/){target=_blank}

* Kafka broker จะรันอยู่ที่ port 9092
* Schema registry จะรันอยู่ที่ port 8081

## Running a Producer

```bash
python json_producer.py -b localhost:9092 -s http://localhost:8081 -t topic_52
```

## Running a Consumer

```bash
python json_consumer.py -b localhost:9092 -s http://localhost:8081 -t topic_52 -g my-group
```

## References

* [Tutorial: Use Schema Registry on Confluent Platform to Implement Schemas for a Client Application](https://docs.confluent.io/platform/current/schema-registry/schema_registry_onprem_tutorial.html){target=_blank}
