
import re
def phonevalidate(phone):
    r = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
    if r.match(phone):
        return True
    else: 
        return False
