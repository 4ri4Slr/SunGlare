# Glare Detection Using Sensor Meta Data Using Flask

## Problem
A manufacturer of automotive vision systems is developing a vision system (camera + object detection module). The machine learning engineers have developed an algorithm and want to test it for direct sun-glare conditions when the camera is installed in a forward-facing position. A direct glare is a condition that creates difficulty of detecting objects in the presence of bright light

The engineers have access to a large repository of high-resolution images that is collected from many hours of driving. They want to select a subset of these images that potentially has direct sun-glare condition in them. Instead of processing the images directly, they want to only use image metadata to examine the glare condition. Each image comes with the following metadata: 
 
-	“lat”: a float between -90 to 90 that shows the latitude in which the image was taken 
-	“lon”: a float between -180 to 180 that shows the longitude in which the image was taken - 	“epoch”: Linux epoch in second 
-	“orientation”: a float between -180 to 180 the east-ward orientation of car travel from true north. 0 means north. 90 is east and -90 is west 

Here is an example of an image metadata: 
```
{ 
 	“lat”: 49.2699648 
 	“lon”: -123.1290368 
 	“epoch”: 1588704959.321 
 	“orientation”: -10.2 
} 
```
 We are interested in a REST API (using either Flask or Django libraries) that process the metadata requests and determines if there is a possibility of direct glare in the associated image or not. We assume there is a possibility of direct glare if:  
 
1-	Azimuthal difference between sun and the direction of the car travel (and hence the direction of forward- facing camera) is less than 30 degrees AND 
 
2-	Altitude of the sun is less than 45 degrees.  

 ```
Request: POST 0.0.0.0:5000/detect_glare -d  
{ 
 	“lat”: 49.2699648 
 	“lon”: -123.1290368 
 	“epoch”: 1588704959.321 
 	“orientation”: -10.2 
} 
Response:  
{  
  “glare”: “false”, 
} 
 ```


### Installation
The required packages can be installed using requirements.txt

    $ pip install -r requirements.txt

### Solution Description 
The only package outside the conventional Flask ecosystem is `pyEphem` that is used 
to calculate the azimuth and elevation angles of the sun give
a set of coordinates and time. 

`Flask_app.py` creates a REST API where the server
receives a json file as a POST request from the client and calls the function
`is_glare` to calculate and send back the response regarding the glare condition.
A more accurate implementation should consider the elevation of the observer 
as well as the reference point of the sun when crossing the geometrical horizon during sunrise.
