#!/bin/sh

if [ "$1" = "" ] || [ "$2" = "" ]; then
    echo "usage $0 <ssid> <password>"
    exit 0
fi

rm /etc/wpa_supplicant/wpa_supplicant.conf

echo "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev">>/etc/wpa_supplicant/wpa_supplicant.conf
echo "update_config=1">>/etc/wpa_supplicant/wpa_supplicant.conf
echo "country=IN">>/etc/wpa_supplicant/wpa_supplicant.conf

echo "network={">>/etc/wpa_supplicant/wpa_supplicant.conf
echo "ssid=\"$1\"">>/etc/wpa_supplicant/wpa_supplicant.conf
echo "psk=\"$2\"">>/etc/wpa_supplicant/wpa_supplicant.conf
echo "key_mgmt=WPA-PS"K>>/etc/wpa_supplicant/wpa_supplicant.conf
echo "}">>/etc/wpa_supplicant/wpa_supplicant.conf