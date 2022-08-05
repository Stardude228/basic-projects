"==================CRUD=================="
# Create
# Read
# Update
# Delete
from utils import validate_id
from utils import read_db, write_db

database = read_db('db.json')

def my_read(user_id: int):
    """
    Accepts a user id.
    Displays his name and info.
    If there is no such id in database the exception will be raised.
    """
    validate_id(database, user_id)
    name = database[user_id]['name']
    info = database[user_id]['info']
    print(
        f"""
        ===={user_id}====
        Name: {name}
        Info: {info}
        ===========
        """)

def my_create():
    """
    Requests a data from user.
    Record in database.
    """
    from utils import generate_id, validate_passwords
    name = input('Type your name: ')
    password = input('Type your password: ')
    password2 = input('Type your validation password: ')
    validate_passwords(password, password2)
    info = input('Type information about yourself: ')
    id_ = generate_id(database.keys())
    database[id_] = {
        'Name': name,
        'Password': password,
        'Info': info,
    }
    print('You been added to python21 successfully!')
    write_db('db.json', database)

def my_delete(user_id: int):
    """
    Accepts an id of a user.
    If there is already exists such a user, he will be deleted.
    If there is no such a user, exeception will be raised.
    """
    validate_id(database.keys(), user_id)
    del database[user_id]
    print(f'{user_id} was deleted successfully deleted!')
    write_db('db.json', database)

def my_update(user_id):
    """
    Accepts a user id.
    Prints old data.
    Accepts a new data.
    Changes in database.
    """
    validate_id(database.keys(), user_id)
    my_read(user_id)
    # Accepts a new data
    name = input('Type your name: ')
    info = input('Type information about yourself: ')
    # Change a data
    database[user_id]['name'] = name
    database[user_id]['info'] = info
    my_read(user_id)
    write_db('db.json', database)
