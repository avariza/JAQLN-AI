"""Performs requests to the Open Street Maps API."""
import requests, json
from shapely.geometry import Polygon, MultiPolygon
import numpy as np
import folium

class OpenStreetMap():
    def __init__(self, osm_id = None, country = None, city = None, state = None, county = None, query = None):
        """
        The function takes in a number of parameters, and uses them to query the Overpass API. The
        results are then stored in a dictionary called `self.metadata`
        
        :param osm_id: The OSM ID of the area you want to get the shape of
        :param custom_shape: a geojson object that you want to use as the boundary for the area
        :param union: If True, the resulting shape will be the union of all the shapes returned by the
        query. If False, the resulting shape will be the intersection of all the shapes returned by the
        query, defaults to True (optional)
        :param country: The name of the country
        :param city: The name of the city you want to get the shape of
        :param state: The state you want to get data for
        :param county: The name of the county
        :param query: A string that will be used to search for a place
        """
        self.params = {"osm_ids": osm_id,
                       "country" : country,
                       "city" : city,
                       "county" : county,
                       "state" : state,
                       "q" : query,
                       "polygon_geojson" : 1,
                       "format" : "json"
                      }
        self.metadata = self._get_metadata()
        self.osm_id = osm_id
        self.shape_geo = self.get_geo_shape()
        
        
    def _get_metadata(self):
        """
        > The function takes a list of parameters and uses them to query the OpenStreetMap API. The
        function returns a dictionary of metadata about the location
        :return: A json object with the metadata of the location.
        """
       
        if self.params.get("osm_ids"):
            endpoint_url = f"https://nominatim.openstreetmap.org/lookup"
        else:
            endpoint_url = f"https://nominatim.openstreetmap.org/search"
        res = requests.get(endpoint_url, params = self.params)
        results =  json.loads(res.content)
        for r in results:
            if r.get("type") and r.get("type") == 'administrative':     
                return r
        return None
    
    def get_geo_shape(self):
        """
        > Extract city polygon coordinates from city metadata and return a shapely object
        :return: A GeoJSON object
        """
       
        self.shape_type = self.metadata.get('geojson', {}).get('type')
        self.shape_coordinates = self.metadata.get('geojson', {}).get('coordinates')

        dispatcher = {
                    'Polygon' : lambda coordinates : Polygon(coordinates[0]),
                    'MultiPolygon': lambda coordinates : MultiPolygon([Polygon(r[0]) for r in coordinates])
                   }
        oms_geo_shape = dispatcher[self.shape_type](self.shape_coordinates)
        self.shape_geo = oms_geo_shape
        return self.shape_geo
               
    def get_geo_center_location(self, administrative = False):
        """
        > This function returns the center of the city's polygon
        
        :param administrative: If True, the city center is the administrative center of the city. If
        False, the city center is the geometric center of the city, defaults to False (optional)
        :return: The centroid of the city.
        """
        if administrative:
            lat = float(self.metadata.get('lat'))
            lng = float(self.metadata.get('lon'))
            self.geo_center = (lat,lng)
            return self.geo_center
        else:
            self.geo_center = self.shape_geo.centroid   
            return (self.geo_center.y, self.geo_center.x)
    
    def plot_geo_items(self):
        """
        It takes a GeoDataFrame, and returns a folium map with the centroids of the GeoDataFrame plotted
        as circles, and the GeoDataFrame's shape plotted as a polygon
        :return: A map object
        """
        m = folium.Map(location=self.get_geo_center_location(), zoom_start=3, tiles='OpenStreetMap')
        for c in self.centroids:
            folium.CircleMarker(location=[c[0], c[1]],
                                radius=1,
                                weight=5).add_to(m)
        poly = self.shape_geo
        return m
