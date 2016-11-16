sudo rm -f ~/iSDX/xrs/ribs/*.db
sudo killall python
sudo killall exabgp
sudo fuser -k 6633/tcp
python ~/endeavour/iSDX/pctrl/clean_mongo.py
