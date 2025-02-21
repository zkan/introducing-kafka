# Starting Kafka on Local

คำสั่ง start Zookeeper

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

คำสั่ง start Kafka

```bash
bin/kafka-server-start.sh config/server.properties
```

ในกรณีที่ตั้ง Kafka ขึ้นมาเอง แล้วอยากให้เข้าถึงได้จากภายนอก ให้แก้ที่ไฟล์ `config/server.properties` ปรับ `listeners` ให้เป็น `0.0.0.0` และ `advertised.listeners` ให้เป็น Public IP ของเครื่อง

```
############################# Socket Server Settings #############################

# The address the socket server listens on. It will get the value returned from
# java.net.InetAddress.getCanonicalHostName() if not configured.
#   FORMAT:
#     listeners = listener_name://host_name:port
#   EXAMPLE:
#     listeners = PLAINTEXT://your.host.name:9092
listeners=PLAINTEXT://0.0.0.0:9092

# Hostname and port the broker will advertise to producers and consumers. If not set,
# it uses the value for "listeners" if configured.  Otherwise, it will use the value
# returned from java.net.InetAddress.getCanonicalHostName().
advertised.listeners=PLAINTEXT://13.212.136.239:9092
```