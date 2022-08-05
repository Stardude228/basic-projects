def login_required(obj):
    if not obj.is_authorized:
        raise Exception('User is not authorized')