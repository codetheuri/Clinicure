""" sample docstring

$DESCRIPTION

$AUTHOR

"""

import argparse
from Logger import logger


def main():
    """ A sample main method """
    logger.critical("critical")
    logger.error("error")
    logger.warning("warning")
    logger.info("info")
    logger.debug("debug")
    print("Welcome to $PROJECT_NAME")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="$DESCRIPTION")
    exit(main())
