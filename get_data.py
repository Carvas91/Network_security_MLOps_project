import os
import sys
import json

from dotenv import load_dotenv


import certifi
import pandas as pd
import numpy as np
import pymongo 


from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkDataExtract(e,sys)
    def csv_tojson_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworkDataExtract(e, sys)
    def pushing_data_to_mongo(self):
        try:
            pass
        except Exception as e:
            raise NetworkDataExtract(e, sys)
    if __name__ == '__main__':
        pass
        