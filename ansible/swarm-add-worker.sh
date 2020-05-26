#!/bin/bash

IP1=xxx
IP4=xxx
token=xxxxxxxxxx

ssh -i xxx.pem ubuntu@${IP4} sudo docker swarm join --token ${token}  ${IP1}:2377