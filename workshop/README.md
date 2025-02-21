# Kafka Workshop

## Getting Started

```bash
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
tar xvf kafka_2.13-3.9.0.tgz
cd kafka_2.13-3.9.0/
```

### Start Zookeeper server

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka server

```bash
bin/kafka-server-start.sh config/server.properties
```