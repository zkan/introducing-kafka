# Python for Kafka

ในเวิร์คชอปนี้เราจะใช้ [Confluent's Kafka Python
client](https://github.com/confluentinc/confluent-kafka-python){target=_blank}
และโค้ดที่ใช้ในเวิร์คชอปนี้จะอยู่ที่โฟลเดอร์ `workshop/` ดังนั้นให้เราเข้าไปที่โฟลเดอร์นั้นก่อน

## Installation

สร้าง Python virtual environment ก่อน โดยใช้คำสั่ง

```bash
python -m venv ENV
source ENV/bin/activate
```

เสร็จแล้วสั่งคำสั่งด้านล่างนี้

```bash
pip install -r requirements.txt
```

หรือถ้าจะติดตั้งเองโดยไม่ใช่ไฟล์ `requirements.txt` ก็ใช้คำสั่ง

```bash
pip install confluent-kafka==2.8.0 six==1.17.0
```

## Running a Producer

```bash
python producer.py
```

## Running a Consumer

```bash
python consumer.py
```
