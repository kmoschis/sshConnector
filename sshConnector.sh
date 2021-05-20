#!/bin/bash
# Requires sshpass

USERNAME1="root"
USERNAME2="admin"
USERNAME3="user"
PASSWORD="password"
IPADDRESSES=( 192.168.0.X 192.168.0.X )

for IP in "${IPADDRESSES[@]}";
do
    {
        echo $USERNAME1@$IP
        sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no $USERNAME1@$IP "hostname;date" #Do command to get config
    } || {
        echo $USERNAME2@$IP
        sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no $USERNAME2@$IP "hostname;date" #Do command to get config
    } || {
        echo $USERNAME3@$IP
        sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no $USERNAME3@$IP "hostname;date" #Do command to get config
    }

done