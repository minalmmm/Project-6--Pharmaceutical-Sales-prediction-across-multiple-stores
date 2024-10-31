import sys
import traceback
from src.logger import logging

# Custom Exception class
class CustomException(Exception):
    def _init_(self, error_message, error_detail: sys):
        # Error message with details
        self.error_message = self.error_message_detail(error_message, error_detail)
        super()._init_(self.error_message)

    # Function to capture detailed error information
    def error_message_detail(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()  # Get exception traceback details
        file_name = exc_tb.tb_frame.f_code.co_filename  # Get file name
        line_number = exc_tb.tb_lineno  # Get line number of the exception

        # Formatting the error message correctly with arguments
        error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, line_number, str(error_message)
        )
        return error_message
    
    def _str_(self):
        return self.error_message

