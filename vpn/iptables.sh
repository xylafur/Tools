#!/bin/bash

iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP


iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -i tun+ -j ACCEPT
iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT



iptables -A OUTPUT -o lo -j ACCEPT
iptables -A OUTPUT -d 209.222.18.222/32 -j ACCEPT
iptables -A OUTPUT -d 209.222.18.218/32 -j ACCEPT

#iptables -A OUTPUT -p udp  --dport 1197 -j ACCEPT
#iptables -A OUTPUT -p tcp --dport 1197 -j ACCEPT
iptables -A OUTPUT -p udp --dport 1198 -j ACCEPT
#iptables -A OUTPUT -p tcp --dport 1198 -j ACCEPT

iptables -A OUTPUT -o tun+ -j ACCEPT
iptables -A OUTPUT -d 192.168.0.0/24 -j ACCEPT
iptables -A OUTPUT -j REJECT --reject-with icmp-net-unreachable
