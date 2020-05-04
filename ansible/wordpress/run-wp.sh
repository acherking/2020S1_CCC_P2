#!/bin/bash

. ./openrc.sh; ansible-playbook -i hosts -u ubuntu --key-file=/Users/achs/Desktop/2020S1/CCC/Assignments/A2/key_pair/wzx2.pem wordpress.yaml
