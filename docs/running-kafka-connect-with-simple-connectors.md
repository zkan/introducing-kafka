# Running Kafka Connect with Simple Connectors

ในเวิร์คชอปนี้เราจะลองเล่น Kafka Connect แบบเรียบร้อย โดยเราจะ import ข้อมูลจากไฟล์เข้าไปที่ topic และ export ข้อมูลจาก topic ไปที่ไฟล์

ก่อนที่จะรัน Kafka Connect ขึ้นมา เราต้องมีตัว connector ก่อน ในที่นี้เราจะใช้ `connect-file-3.9.0.jar` เพื่อเชื่อมต่อไปยังไฟล์ โดยให้เราปรับแก้ไฟล์ configuration ที่ชื่อ `config/connect-standalone.properties` แล้วเซตค่า `plugin.path` ตามนี้

```
plugin.path=libs/connect-file-3.9.0.jar
```

ที่ไฟล์ `config/connect-file-source.properties` และ `config/connect-file-sink.properties` จะเป็น configuration ของ source และ sink ที่เราจะไป connect ด้วยตามลำดับ

โดย source ที่ตั้งไว้ใน configuration จะเป็นไฟล์ที่ชื่อ `test.txt` ดังนั้นให้เราสร้างไฟล์นี้ขึ้นมาก่อนด้วยคำสั่งด้านล่างนี้

```bash
echo "hello" > test.txt
```

ส่วน sink จะเป็นไฟล์ชื่อ `test.sink.txt` และ topic จะชื่อ `connect-test`

หลังจากนั้น เพื่อความง่ายเราจะรัน Kafka Connect ขึ้นมาแบบ standalone โดยใช้คำสั่งด้านล่างนี้ (ในขณะที่ Kafka server และ ZooKeeper ยังรันอยู่)

```bash
bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
```

พอรันเสร็จเราจะเห็นว่ามีไฟล์ `test.sink.txt` เกิดขึ้นมา แล้วถ้าเราแก้ไฟล์ต้นทาง `test.txt` เราก็ควรจะเห็นข้อมูลในไฟล์ `test.sink.txt` มีการเปลี่ยนแปลง ทดสอบได้ด้วยคำสั่งด้านล่างนี้

```bash
echo "another hello" >> test.txt
```

นอกจากนี้เรายังสามารถรัน consumer ขึ้นมาเพื่อดึง message จาก topic `connect-test` ได้อีกด้วย ให้ใช้คำสั่งตามนี้

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic connect-test --from-beginning
```

แล้วลองแก้ไขไฟล์ source ตามคำสั่งด้านล่างนี้ แล้วดูผลลัพธ์

```bash
echo "whassup" >> test.txt
```
