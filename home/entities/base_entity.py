import re

class BaseEntity():

    def validate_mobile_number(mobile_number):
        # pattern = re.compile(r'^\d{10}$')
        # return bool(pattern.match(mobile_number))
        pattern = r'^\d{10}$'
        return re.match(pattern, mobile_number)
    
    def validate_email(email):        
        pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(pattern.match(email))
    
    
    
    


    