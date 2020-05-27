#!/bin/bash

export IP1=172.26.132.113
export IP4=172.26.130.25

ssh -i ../key_pair/wzx2.pem ubuntu@${IP1} sudo docker node ls
echo 
echo
ssh -i ../key_pair/wzx2.pem ubuntu@${IP4} sudo docker swarm leave
echo
echo
sleep 30
ssh -i ../key_pair/wzx2.pem ubuntu@${IP1} sudo docker node rm demo-4
ssh -i ../key_pair/wzx2.pem ubuntu@${IP1} sudo docker node ls