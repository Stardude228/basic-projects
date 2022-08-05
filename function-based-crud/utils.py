"File with additional functions"

import json


def generate_id(ids):
    """Accepts a list of existing ids. 
    Returns new id in range from 100 to 1000"""
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids:
        id_ = random.randint(100, 999)
    return str(id_)

def validate_passwords(p1, p2):
    """
    Accepts 2 passwords and if they do not match the exception will be raised.
    """
    if p1 != p2:
        raise Exception("Passwords do not match!")

def validate_id(ids, user_id):
    """
    Accepts a list of existing ids and user id that has to be checked.
    If there is no such an id the exception will be raised.
    """
    if user_id not in ids:
        raise Exception("There is no such an id!") 
    # We can use KeyError but it is not recommended
    
def read_db(file_name):
    """
    Accepts a name of a file.
    Returns a data from database in python object view.
    """
    import json
    with open(file_name, "r") as file:
        db = json.load(file)
    return db

def write_db(file_name, data):
    """
    Accepts a name of a file and data for the record.
    Records this data into the file.
    """
    import json
    with open(file_name, 'w') as file:
        json.dump(data, file)
    

