def convert_to_boolean(val):
    if type(val) == bool:
        return val
    elif type(val) == str:
        return val.lower() == "true"