def createRecord(name, dob, password, address, phone):
    newRecord = {}
    newRecord["Name"] = name
    newRecord["Date of Birth"] = dob
    newRecord["Password"] = password
    newRecord["Address"] = address
    newRecord["Phone"] = phone
    return newRecord
