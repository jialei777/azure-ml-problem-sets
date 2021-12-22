# To-Do: import libraries
import logging
from shrike.compliant_logging import enable_compliant_logging 
from shrike.compliant_logging.constants import DataCategory
import datetime

def main():
    """The main function"""
    # To-Do: initialize logger class and log

    now = datetime.datetime.now()

    enable_compliant_logging()
    logger = logging.getLogger(__name__)

    logger.info("This is public", category=DataCategory.PUBLIC)
    logger.info("This is private", category=DataCategory.PRIVATE)

    logger.info("Hello, world from Jialei! -public", category=DataCategory.PUBLIC)
    logger.info("Hello, world from Jialei! -private", category=DataCategory.PRIVATE)

    logger.info("   -- time: -public" + str(now), category=DataCategory.PUBLIC)
    logger.info("   -- time: -private" + str(now), category=DataCategory.PRIVATE)



if __name__ == "__main__":
    main()
