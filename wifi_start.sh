#!/bin/sh
wifidev="wlan0" 
ip link set dev "$wifidev" down
ip addr flush dev "$wifidev"
ip link set dev "$wifidev" up
dhcpcd  -n "$wifidev" >/dev/null 2>&1
wpa_supplicant -B -i "$wifidev" -c /etc/wpa_supplicant/wpa_supplicant.conf
