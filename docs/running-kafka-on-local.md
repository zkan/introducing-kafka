# Running Kafka on Local

## Downloading Kafka

ก่อนเริ่มให้เราดาวน์โหลด Kafka ลงมาบนเครื่องก่อน โดยใข้คำสั่งด้านล่างนี้ หรือเข้าไปดาวน์โหลดไฟล์
binary เองได้ที่[เว็บไซต์ Kafka](https://kafka.apache.org/downloads){target=_blank}
โดยตรง

```bash
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
tar xvf kafka_2.13-3.9.0.tgz
cd kafka_2.13-3.9.0/
```

ภายในโฟลเดอร์ `kafka_2.13-3.9.0/` จะมีหน้าตาประมาณนี้

```
.
├── LICENSE
├── NOTICE
├── bin/
├── config/
├── libs/
├── licenses/
├── logs/
└── site-docs/
```

แล้วจะมีโฟลเดอร์ย่อยที่เราจะใช้เป็นหลักอยู่ 2 โฟลเดอร์คือ

1. `bin/` เป็นโฟลเดอร์ที่เก็บ Bash script ต่าง ๆ ที่เราจะใช้งาน เช่น script ที่ใช้สำหรับการรัน
   Kafka เป็นต้น
1. `config/` เป็นโฟลเดอร์ที่เก็บไฟล์ configuration ต่าง ๆ เช่น configuration ของ Kafka
   server เป็นต้น

ตลอดทั้งเวิร์คชอปที่เราใช้งาน Bash script ของ Kafka เราจะสั่งคำสั่งอยู่ภายใต้โฟลเดอร์
`kafka_2.13-3.9.0/` เท่านั้น ถ้าไม่ได้อยู่ภายใต้โฟลเดอร์นั้นแล้ว อาจจะต้องมีการปรับคำสั่งต่าง ๆ
ที่ใช้ในเวิร์คชอปนี้เอง

## Starting ZooKeeper

เปิด terminal หรือ command prompt ขึ้นมาแล้วรันคำสั่งด้านล่างนี้

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

* ZooKeeper จะใช้ port 2181
* Logs จะอยู่ที่ `/tmp/zookeeper`

!!! note

    ในการรัน Kafka นั้น เราจำเป็นต้องรัน ZooKeeper ขึ้นมาก่อน เพราะ Kafka ต้องใช้งาน
    และเวลาที่เราจะเลิกใช้งาน เราก็ต้องปิด Kafka ก่อน แล้วค่อยปิด ZooKeeper

## Starting Kafka

เปิด terminal หรือ command prompt ขึ้นมาแล้วรันคำสั่งด้านล่างนี้

```bash
bin/kafka-server-start.sh config/server.properties
```

* Kafka จะใช้ port 9092
* Logs จะอยู่ที่ `/tmp/kafka-logs`

!!! tip

    ในกรณีที่ตั้ง Kafka ขึ้นมาเอง แล้วอยากให้เข้าถึงได้จากภายนอก ให้แก้ที่ไฟล์
    `config/server.properties` ปรับ `listeners` ให้เป็น `0.0.0.0` และ
    `advertised.listeners` ให้เป็น Public IP ของเครื่อง เช่น `13.212.136.239` เป็นต้น

    ```
    ############################# Socket Server Settings #############################

    # The address the socket server listens on. If not configured, the host name will be equal to the value of
    # java.net.InetAddress.getCanonicalHostName(), with PLAINTEXT listener name, and port 9092.
    #   FORMAT:
    #     listeners = listener_name://host_name:port
    #   EXAMPLE:
    #     listeners = PLAINTEXT://your.host.name:9092
    listeners=PLAINTEXT://0.0.0.0:9092

    # Listener name, hostname and port the broker will advertise to clients.
    # If not set, it uses the value for "listeners".
    advertised.listeners=PLAINTEXT://13.212.136.239:9092
    ```
