# Imports
import argparse
import configparser

# Logging
import logging
logger = logging.getLogger(__name__)

# Constants
CONF = 'config.conf'

# Functions

# Program
def main(conf:str=CONF, *args, **kwargs):
    exit_code = 0

    # load config
    config = configparser.RawConfigParser()
    config.read(conf)

    # setup logging
    logging.basicConfig(**config['Logging'])
    logger.info(f"Loaded config form {conf}")
    logger.info(f"Log level: {logging.getLevelName(logging.root.level)}")

    # [TODO] write program

    return exit_code



# Entry point
if __name__ == '__main__':
    # process command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf', type=str, default=CONF, 
        help='path to config file')

    exit(main(**vars(parser.parse_args())))