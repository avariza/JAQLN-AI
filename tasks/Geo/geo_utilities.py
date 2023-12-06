"""Converts distances into one format to another
    For example:
    distance in km to disance in coordinates degrees
"""

import math


def km_to_degrees(distance_km:int = None):
    """
    > This function converts a distance in kilometers to a distance in degrees.
    
    :param distance_km: The distance in kilometers
    :type distance_km: str
    :return: The distance in degrees
    """
    # Earth's radius in kilometers
    R = 6371  
    distance_degrees = (distance_km / R) * (180 / math.pi)
    return distance_degrees


def m_to_km(distance_m:int = None):
    """
    `m_to_km` converts a distance in meters to kilometers
    
    :param distance_m: The distance in meters
    :type distance_m: str
    :return: the distance in kilometers.
    """
    kilometers = distance_m / 1000
    return kilometers


def decimal_to_km(decimal_distance:int = None):
    """
    `Convert decimal distance into km`
    
    This is a good summary because it's short, and it tells you what the function does
    
    :param decimal_distance: The decimal distance to convert to km
    :type decimal_distance: str
    :return: the kilometers.
    """
    kilometers = (decimal_distance*11.1) / 0.1
    return kilometers


def decimal_to_dms(decimal_coord:str = None):
    """
    > Convert a decimal coordinate to degrees, minutes, seconds
    
    :param decimal_coord: The decimal coordinate to convert
    :type decimal_coord: str
    :return: A tuple of the degrees, minutes, and seconds of the decimal coordinate.
    """
    is_positive = decimal_coord >= 0
    decimal_coord = abs(decimal_coord)
    degrees = int(decimal_coord)
    minutes = int((decimal_coord - degrees) * 60)
    seconds = (((decimal_coord - degrees) * 60) - minutes) * 60
    if is_positive:
        return (degrees, minutes, seconds)
    else:
        return (-degrees, minutes, seconds)
