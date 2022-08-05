def get_obj_or_404(model, attr, value):
    found = False

    for object_ in model.objects:
        object_value = getattr(object_, attr)
        if object_value == value:
            found = True
            break

    if not found:
        raise Exception(f'404 {model.__name__} Not Found')
    
    return object_