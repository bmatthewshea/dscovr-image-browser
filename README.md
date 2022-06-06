# DSCOVR:EPIC - Image Browser

To run this app:

Clone this repository.

Go into the downloaded folder and run the builtin webserver:

```
export FLASK_APP=app.py; \
export FLASK_ENV=development; \
flask run -h 0.0.0.0 -p 8000
```



Open a browser on same machine (or same local network):

Same machine:

http://127.0.0.1:8000

From a machine on same LAN (example - use your own network address!):

http://192.168.200.1:8000



- The image link will open the image in a new tab.

- The Latitude/Longitude link will open a Google Maps link to give a conventional map based on image coordinates.


![](https://i.imgur.com/PK0ijDb.jpg)

![](https://i.imgur.com/bZfie8o.png)

