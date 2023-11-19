import sys
import os
import logging
'''
The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.
'''
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # getcwd CORRENT WORKING DIRECTORY
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)


def error_message_detail(error,error_detail:sys):
    _,_,exc_tab=error_detail.exc_info()    ## will tell all information about theexeption , like which file and whih line it occured
    file_name=exc_tab.tb_frame.f_code.co_filename
    error_message="Error accured in python script name [{0}] line number[{1}] error message [{2}]".format(
        file_name,exc_tab.tb_lineno,str(error)

        )
    
    return error_message 
    
class CustomException(Exception):   
    def __init__(self,error_message,error_detail:sys) :
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message   
    

'''if __name__=="__main__":
     
     try:
        a=1/0
     except Exception as e:
        logging.info("Divide by zero")
        raise CustomException (e,sys)
        '''
            