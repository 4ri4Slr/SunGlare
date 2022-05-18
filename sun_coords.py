import numpy as np
import ephem
from datetime import datetime
import time

def is_glare(inputs):

    frame_time = inputs['epoch']
    latitude = inputs['lat']
    longitude = inputs['lon']
    orientation = (inputs['orientation'] + 180) % 360 - 180

    if not (0 < frame_time < time.time()):
        raise ValueError('Please enter a valid epoch')

    if not (-180 < longitude < 180):
        raise ValueError('Please enter a valid longitude in range (-180,180)')

    if not (0 < latitude < 90):
        raise ValueError('Please enter a valid latitude in range (0, 90)')

    """
    Calculate the solar position using the PyEphem package.

    Parameters
    ----------
    frame_time : unix epoch
    latitude : float
        Latitude in decimal degrees. Positive north of equator, negative
        to south.
    longitude : float
        Longitude in decimal degrees. Positive east of prime meridian,
        negative to west.
    Returns
    -------
    is_glare: Bool 
        Whether sun glare is present in the frame based on calculated azimuth,
        and elevation

    """

    current_time = datetime.utcfromtimestamp(frame_time).strftime('%Y-%m-%d %H:%M:%S')
    obs, sun = ephem_setup(latitude, longitude)
    obs.date = ephem.Date(current_time)
    sun.compute(obs)
    print("Sun azimuth is %s and sun altitude is %s" %(sun.az, sun.alt))

    return (np.degrees(sun.az) - orientation < 30) and (np.degrees(sun.alt) < 45)


def ephem_setup(latitude, longitude):

    # initialize a PyEphem observer
    obs = ephem.Observer()
    obs.lat = str(latitude)
    obs.lon = str(longitude)


    # the PyEphem sun
    sun = ephem.Sun()
    return obs, sun
