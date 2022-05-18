# Glare Detection Using Sensor Meta Data Using Flask

### Installation
The required packages can be installed using requirements.txt

    $ pip install -r requirements.txt

### Description 
The only package outside the conventional Flask ecosystem is `pyEphem` that is used 
to calculate the azimuth and elevation angles of the sun give
a set of coordinates and time. 

`Flask_app.py` creates a REST API where the server
receives a json file as a POST request from the client and calls the function
`is_glare` to calculate and send back the response regarding the glare condition.
A more accurate implementation should consider the elevation of the observer 
as well as the reference point of the sun when crossing the geometrical horizon during sunrise.
