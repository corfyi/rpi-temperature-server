
import sys
import json
from tornado.options import define, options
from server import server, config

# parse command line arguments
define('config', default=config.cfg_file, help='config file')
options.parse_command_line()

# load config data from specified file
try:
    with open(options.config) as f:
        config_data = json.load(f)
except Exception as e:
    print('Error loading config -', e)
    sys.exit(1)

# set the data in config
config.set_data(config_data)

# run the server!!
if __name__ == '__main__':
    server.run()
