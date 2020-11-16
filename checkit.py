import argparse
import logging
import os
import sys
import yaml

_SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
_LOG_FILE = os.path.join(_SCRIPT_FOLDER, 'checkit.log')

class Check:
    pass

class DNSCheck(Check):
    pass

class URICheck(Check):
    pass

# Configure logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)
logging_formatter = logging.Formatter(
        fmt='[%(asctime)s] (%(levelname)8s) %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
        )
# Logging to stdout, info
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(logging_formatter)
log.addHandler(stdout_handler)
# Logging to file, debug
file_handler = logging.FileHandler(_LOG_FILE)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging_formatter)
log.addHandler(file_handler)
# End configure logging

log.info('Starting.')
log.info(f"Writing debug log to {_LOG_FILE!r}.")

# Get command line arguments
argp = argparse.ArgumentParser()
argp.add_argument('--config', type=str, help='YAML file containing checks.', default=os.path.join(_SCRIPT_FOLDER, 'checkit.yaml'))
args = argp.parse_args()
log.info(f"Reading checks from {os.path.abspath(args.config)!r}.")
# End get command line arguments

# Read YAML from file
try:
    with open(args.config) as config_file:
        try:
            yaml_checks = yaml.safe_load(config_file)
        except yaml.YAMLError as ex:
            log.error(ex)
except FileNotFoundError as ex:
    log.error(ex)
# End read YAML from file

# Parse checks
print(yaml_checks)
# End parse checks

# Clean up
log.info("Done.")
