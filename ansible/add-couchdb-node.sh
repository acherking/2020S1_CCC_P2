#!/bin/bash

IP1=xxx
IP4=xxx

curl -X POST -H "Content-Type: application/json" http://admin:123456@${IP1}:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"123456", "port": 5984, "node_count": "4", "remote_node": "${IP4}", "remote_current_user": "admin", "remote_current_password": "123456" }'
curl -X POST -H "Content-Type: application/json" http://admin:123456@${IP1}:5984/_cluster_setup -d '{"action": "add_node", "host":"${IP4}", "port": 5984, "username": "admin", "password":"123456"}'
curl -XGET http://admin:123456@${IP1}:5984/
curl -X POST -H "Content-Type: application/json" http://admin:123456@${IP1}:5984/_cluster_setup -d '{"action": "finish_cluster"}'
curl http://admin:123456@${IP1}:5984/_cluster_setup
curl http://admin:123456@${IP1}:5984/_membership