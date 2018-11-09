#!/usr/bin/env bash

set -o errexit
set -o nounset

iface=$(networksetup -listnetworkserviceorder |
    egrep 'Hardware Port: (Wi-Fi|AirPort)' |
    tr ')' ' ' |
    awk '{print $5}')

curr_state=$(networksetup -getairportpower "$iface" | awk '{print $4}')

if [[ "$curr_state" == "On" ]]; then
    networksetup -setairportpower "$iface" "off"
    networksetup -setairportpower "$iface" "on"
elif [[ "$curr_state" == "Off" ]]; then
    networksetup -setairportpower "$iface" "on"
    networksetup -setairportpower "$iface" "off"
else
    echo "$iface"
    exit 1
fi