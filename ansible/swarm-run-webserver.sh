#!/bin/bash

IP1=xxx

ssh -i xxx.pem ubuntu@${IP1} sudo docker service create -d \
  --replicas=3 \
  --name web-service \
  -p 8000:8000 \
  acherking/cccp2web:2.0 \
  python manage.py runserver 0.0.0.0:8000