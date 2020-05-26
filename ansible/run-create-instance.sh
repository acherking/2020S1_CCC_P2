#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass create-instance.yaml