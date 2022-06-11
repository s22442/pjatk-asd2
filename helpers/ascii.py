def asciify_dict_keys(dictionary: dict):
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[ord(key)] = value
    return new_dictionary
