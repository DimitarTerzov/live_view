"""The Photo To Cloud System Configuration file."""
USER_ID = '1'
# URL = "https://www.laburnumsystems.com/phototocloud/download_json.php?table="
URL = "http://127.0.0.1:8000/download_json?table="
runServerCommand = "sudo -u pi /usr/bin/python3 /home/pi/Desktop/LiveView/web/Laburnum_Systems/manage.py runserver 0.0.0.0:8000 &"
