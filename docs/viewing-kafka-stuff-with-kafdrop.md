# Viewing Kafka Stuff with Kafdrop

> Kafdrop is a web UI for viewing Kafka topics and browsing consumer groups.
> The tool displays information such as brokers, topics, partitions, consumers,
> and lets you view messages. See
> [GitHub](https://github.com/obsidiandynamics/kafdrop){target=_blank} for more
> detail.

เราใช้ไฟล์ `docker-compose.yml` เดียวกับเวิร์คชอป [Python for Kafka with Schema
Registry (on Confluent
Platform)](python-for-kafka-with-schema-registry-on-confluent-platform.md)
ซึ่งส่วนที่รัน Kafdrop ขึ้นมาคือ

```yaml
  kafdrop:
    image: obsidiandynamics/kafdrop:4.1.0
    depends_on:
      - broker
    ports:
      - 9000:9000
    environment:
      KAFKA_BROKERCONNECT: 'broker:29092'
      SERVER_SERVLET_CONTEXTPATH: '/'
```

ดังนั้นให้เรารันคำสั่งด้านล่างนี้ได้เลย

```bash
docker compose up
```

แล้วเข้าหน้า web UI ได้ที่
[http://localhost:9000](http://localhost:9000){target=_blank}
