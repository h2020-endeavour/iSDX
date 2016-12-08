#!/bin/bash

cd ..

wget http://scapy.net/

mv index.html scapy.zip
unzip scapy.zip
cd scapy-2.*
sudo python setup.py install
cd ../iSDX

