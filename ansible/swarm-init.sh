#!/bin/bash

IP1=xxx

ssh -i xxx.pem ubuntu@${IP1} sudo docker swarm init --advertise-addr 