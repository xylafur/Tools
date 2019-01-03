#!/bin/bash

while ifconfig | grep -q tun; do
	sleep 5
done
systemctl stop transmission-daemon.service
