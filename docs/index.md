# Welcome to Kafka Workshop

Kafka is an open-source fault-tolerant, robust distributed event streaming
platform. A single Kafka node is called a *broker*, and multiple Kafka servers
make up a *cluster*. Kafka stores messages written by *producers* in *topics*.
*Consumers* subscribe to topics and contact Kafka to see if messages are
available in those subscribed topics.

## Prerequisites

* Your [GitHub](https://github.com){target=_blank} account
* Workshop Repo: [:material-github: GitHub](https://github.com/zkan/introducing-kafka/){target=_blank}

## Getting Started

Download Kafka

```bash
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
tar xvf kafka_2.13-3.9.0.tgz
cd kafka_2.13-3.9.0/
```

Start Zookeeper server

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Start Kafka server

```bash
bin/kafka-server-start.sh config/server.properties
```
