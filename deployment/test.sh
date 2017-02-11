#!/bin/bash

set -e

echo 'testing connectivity'
sudo -u cif cif --config /home/cif/.cif.yml -p

echo 'testing query'
sudo -u cif cif --config /home/cif/.cif.yml --search example.com

echo 'waiting...'
sleep 5

echo 'testing query'
sudo -u cif cif --config /home/cif/.cif.yml --search example.com

echo 'waiting...'
sleep 5

sudo -u cif cif --config /home/cif/.cif.yml --itype ipv4

sudo -u cif cif --config /home/cif/.cif.yml -q 93.184.216.34

echo 'waiting...'
sleep 5

sudo -u cif cif --config /home/cif/.cif.yml -q 93.184.216.34

sudo su - cif
csirtg-smrt -r /etc/cif/rules/default/csirtg.yml -d --remember --client cif --config /etc/cif/csirtg-smrt.yml
cif --config /home/cif/.cif.yml --provider csirtg.io
exit