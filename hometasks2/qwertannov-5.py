def get_root_property(dictionary, element):

    for key, value in dictionary.items():
        if isinstance(value, list) and element in value:
            return key
        elif isinstance(value, dict):
            result = get_root_property(value, element)
            if result is not None:
                return key

    return None
