
def all_thing_is_obj(value):
    valueType = type(value)
    if (valueType == list):
        print("List :", valueType)
    elif (valueType == tuple):
        print("Tuple :", valueType)
    elif (valueType == set):
        print("Set :", valueType)
    elif (valueType == dict):
        print("Dict :", valueType)
    elif (valueType == str):
        print(value, "is in the kitchen :", valueType)
    else:
        print("Type not found")
    return 42
