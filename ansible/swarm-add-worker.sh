#!/bin/bash

export IP1=172.26.132.113
export IP4=172.26.130.25
export token=SWMTKN-1-1h84n38b35xzff58tb3hh96w4dqnxv1oja7q4vj05r7qlt9fd7-832d3hjjmsbfve9nyho8zgl24

ssh -i ../key_pair/wzx2.pem ubuntu@${IP1} sudo docker node ls
echo 
echo
ssh -i ../key_pair/wzx2.pem ubuntu@${IP4} sudo docker swarm join --token ${token}  ${IP1}:2377
echo
echo
ssh -i ../key_pair/wzx2.pem ubuntu@${IP1} sudo docker node ls