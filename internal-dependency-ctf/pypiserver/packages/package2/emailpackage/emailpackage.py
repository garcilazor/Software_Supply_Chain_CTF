import re
def emailvalidate(email): 
    regex = re.compile('[^@]+@[^@]+\.[^@]+')
    if regex.match(email):
        return True
    else: 
        return False
