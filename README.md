## DSCOVR:EPIC - Image Browser

A browser for "Blue Marble" NASA images.

This is just a small web version of this code:

https://github.com/bmatthewshea/DSCOVR-Blue-Marble

To run this web app:

1. Install [Flask](https://flask.palletsprojects.com/en/stable/installation/ "Flask Installation Page") with venv.

2. Clone this repository.

3. Go into the cloned folder and run the builtin webserver:

```
flask run -h 0.0.0.0 -p 8000
```

4. Open a browser on same machine (or same local network):

    &emsp;Same machine:

    &emsp;http://127.0.0.1:8000

    &emsp;From a machine on same LAN (example - use your own network address!):

    &emsp;http://192.168.200.1:8000


- The image link will open the image in a new tab.

- The Latitude/Longitude link will open a Google Maps link to give a conventional map based on image coordinates.



![](https://i.imgur.com/PK0ijDb.jpg)

![](https://i.imgur.com/bZfie8o.png)

