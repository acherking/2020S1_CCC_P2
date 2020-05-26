#!/bin/bash

IP4=172.26.130.93

ssh -i ../key_pair/wzx2.pem ubuntu@${IP4} sudo docker swarm leave