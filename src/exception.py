'''
    This is the exception handling file where we are writing the code to raise exception and print the error
'''

import sys

def raise_error_message(error, error_details:sys):
    _,_,exec_tb = error_details.exc_info()

    file_name = exec_tb.tb_frame.f_code.co_filename

    error_message = ''' Error has occurred in the python script name {0},
File name {1} with error message {2}
'''.format(file_name, exec_tb.tb_lineno, str(error))
    
    return error_message


class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message = raise_error_message(error_message,error_detail)

    
    def __str__(self):
        return self.error_message    