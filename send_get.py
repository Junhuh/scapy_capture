# !/usr/bin/env python
# -- coding: utf-8 --
from scapy.all import *
# 使用scapy需安装npcap，否则会报错

# 发送报文
# 数据包应用层数据部分
# data = 'Aa'
# 发送报文
# pkt = IP(src="192.168.0.100",dst="192.168.0.1")/UDP(sport=1333,dport=1222) / data
# 间隔2秒发送一次   总共发送6次   发送网卡口：描述
# send(pkt, inter=2, count=6, iface="Realtek RTL8139/810x Family Fast Ethernet NIC")

# 捕获报文
# 监听模式，条件未设置，捕获所有，指定网卡，报文个数200
dpkt  = sniff(filter = '', iface = "Realtek RTL8139/810x Family Fast Ethernet NIC", count = 200)
# 保存报文
wrpcap("demo.pcap", dpkt)