# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        water_stn_converter.py
#
# Purpose:
#    Converts a JSON file created using the water_stn_downloader module to KML/KMZ.
#
#    For the KML, the <Placemark> element will have the following sub-elements:
#              <name>{Station_Name}</name>
#              <description>
#                 link
#              </description>
#              <Point>
#                <coordinates>{Longitude},{Latitude},0</coordinates>
#              </Point>
# 
#    where link is
#    https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}
#
#   Items enclosed by { } are the keys in the dictionary associated with
#   each feature (a key:value dictionary of values).
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import os
import json

# Path to folder containing this script and make it the current folder
#
_script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(_script_folder)

in_json_filename = ''
out_kml_filename = ''


def json_to_kml():
    """Converts a JSON file created using the water_stn_downloader module
    to KML"""
    # TODO: Extract the information from the JSON file and write to KML
    #       Write the KML Header
    #       Open the in_json_filename, loop through all "features",
    #       extract necessary data to create placemarks, and write them 
    #       to the kml file one at a time


def load_json_file_to_dict():
    """Use json.load(file_object) to convert the contents of in_json_filename
    to a Python dictionary.  Return the resulting dictionary.
    """
    # TODO:  Use with to open in_json_filename and use that file object as an
    # argument to json.load.  The json.load method will return a Python dict
    # with nested lists and dictionaries


def get_values_from_feature(feature):
    """Given a dictionary of feature attributes, return the following:
        Station_Number, Station_name, Longitude, Latitude.
        NOTE:  return x, y, z will return a tuple with values associated with
                              variable x, y, z """


def get_wateroffice_link(station_number):
    """Given a station_number, return the English wateroffice link"""


def get_kml_header():
    """Return the xml header including the Document start tag
    """


def get_kml_footer():
    """Return the document and kml end tags
    """


def get_placemark(name, longitude, latitude, wateroffice_link):
    """Return the KML Placemark element including start and end tags
    """
    # TODO: Create a placemark KML element (HINT:  use f'{...}')