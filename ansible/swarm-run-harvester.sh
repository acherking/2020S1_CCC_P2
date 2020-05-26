#!/bin/bash

IP1=xxx
IP2=xxx
IP3=xxx

ssh -i xxx.pem ubuntu@${IP1} mkdir -p /home/ubuntu/tweet_harvester/data
ssh -i xxx.pem ubuntu@${IP2} mkdir -p /home/ubuntu/tweet_harvester/data
ssh -i xxx.pem ubuntu@${IP3} mkdir -p /home/ubuntu/tweet_harvester/data


ssh -i xxx.pem ubuntu@${IP1} sudo docker service create -d \
  --replicas=1 \
  --name twitter-harvester-mel \
  --mount type=bind,source=/home/ubuntu/tweet_harvester/data,destination=/tweet_harvester/data \
  acherking/cccp2py:1.2 \
  python3 -u melbourne_data.py

ssh -i xxx.pem ubuntu@${IP1} sudo docker service create -d \
  --replicas=1 \
  --name twitter-harvester-au \
  --mount type=bind,source=/home/ubuntu/tweet_harvester/data,destination=/tweet_harvester/data \
  acherking/cccp2py:1.2 \
  python3 -u australia_data.py