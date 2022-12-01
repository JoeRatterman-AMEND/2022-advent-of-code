""" 

Description of this Python script.

Authors: 
Contact:
Date: 
Status

"""

import yaml
import logging

# Function to read in yaml file contents
def read_config(config_file):
  try:
     with open(config_file) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        
        # Read in each parameter; first try to find, if not present catch error and exit
        try:
                example-parameter = config["example-parameter"]
        except KeyError:
          logger.error("No example-parameter found in config")
          exit()
          
        # Read in list parameters (similar to normal)
        try:
                example-parameter = config["example-list"]["item-1"]
        except KeyError:
          logger.error("No example-list item-1 found in config")
          exit()
        
  except FileNotFoundError:
    logger.error('Config file not found') 
