# RFID PROJECT

Project RFID with a Raspberry Pi for Catholic University in Lille.

## LIBRARY PYTHON 

> https://github.com/mxgxw/MFRC522-python

## LAUNCH PROJECT

### BEFORE INSTALLATION

    sudo apt install apache2
    sudo chown -R pi:www-data /var/www/html/
    sudo chmod -R 770 /var/www/html/

### AFTER INSTALLATION

    cd /var/www/html/
    git clone https://github.com/MayuriXx/RFID_project.git 
    cd MFRC522-python
    python Read.py

> check uid.txt in directory MFRC522-python

## Interface web

**Launch apache server**
http://localhost/projet/index.html
