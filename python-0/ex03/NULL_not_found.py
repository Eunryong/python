
def NULL_not_found(value):
    valueType = type(value)
    # if (isinstance(value, type(None))):
    if (value == None):
        print("Noting:", value, valueType)
    elif (isinstance(value, float) and value != value):
        print("Cheese:", value, valueType)
    elif (valueType == int and value == 0):
        print("Zero:", value, valueType)
    elif (value == ""):
        print("Empty:", value, valueType)
    elif (value == False):
        print("Fake:", value, valueType)
    else:
        print("Type not found")
    return 1