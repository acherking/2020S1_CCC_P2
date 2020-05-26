#!/bin/bash

IP1=xxx
IP2=xxx
IP3=xxx
token=xxxxxxxxxx

ssh -i xxx.pem ubuntu@${IP2} sudo docker swarm join --token ${token}  ${IP1}:2377
ssh -i xxx.pem ubuntu@${IP3} sudo docker swarm join --token ${token}  ${IP1}:2377