# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        water_stn_downloader.py
#
# Purpose:     Saves the response from a RESTful request to a .json file.
#              The request is defined by url and params attributes
#
# Author:      David Viljoen
#
# Created:     18/11/2019
# ------------------------------------------------------------------------------

import requests
from requests import HTTPError

url = ''
params = {}
out_json_filename = ''

def download_to_file():
    """Save the response of a RESTful request to a file.  The following global
    attributes are used:
        url = The base URL to the RESTful service
        params = Python dictionary of key value pairs for query parameters
        out_json_filename = file where response to RESTful request will be
                            saved. """

    try:
        response = requests.get(url, params, stream=True, timeout=30)
        response.raise_for_status()
        with open(out_json_filename, 'wb') as out_file:
            # Iterate through the response in 1 MB chunks
            #
            for chunk in response.iter_content(chunk_size=1024*1024):
                # Write each chunk out to the .json file ...
                #
                out_file.write(chunk)
    except HTTPError as http_err:
        return 'HTTPError: {}'.format(http_err)
    except Exception as err:
        return 'Error:'.format(err.message)
    else:
        return 'OK'
