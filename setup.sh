#!/bin/bash
pip install datetime
apt update && apt upgrade
pkg install figlet -y
apt install ruby -y && gem install lolcat
pkg install python -y
pkg install mpv -y
figlet python | lolcat && echo "Installed..............." | lolcat
pkg install toilet -y
figlet toilet  | lolcat && echo "Installed..............." | lolcat
apt install termux-api -y
figlet termux-api | lolcat && echo "Installed..............." | lolcat
clear
echo "Setup Satisfied" | lolcat -as 100
python Alarm.py
