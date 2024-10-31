import logging
import pandas as pd

def initialize_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler('rossmann_sales_forecast.log')
    file_handler.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize the logger
logger = initialize_logger()

# Log the start of your script
logger.info('Starting the Rossmann sales forecast analysis.')

# Load datasets
try:
    store_data = pd.read_csv('C:\\data science material\\project_6\\Notebook\\data\\rossmann-store-sales\\store.csv')
    logger.info('Store data loaded successfully.')
except Exception as e:
    logger.error(f'Error loading store data: {e}')

try:
    train_data = pd.read_csv('C:\\data science material\\project_6\\Notebook\\data\\rossmann-store-sales\\train.csv')
    logger.info('Training data loaded successfully.')
except Exception as e:
    logger.error(f'Error loading training data: {e}')

try:
    test_data = pd.read_csv('C:\\data science material\\project_6\\Notebook\\data\\rossmann-store-sales\\test.csv')
    logger.info('Test data loaded successfully.')
except Exception as e:
    logger.error(f'Error loading test data: {e}')
