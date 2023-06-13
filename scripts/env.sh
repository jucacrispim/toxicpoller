#!/bin/sh

docker run -d --network=host zookeeper:latest
docker run -d --network=host rabbitmq:latest
