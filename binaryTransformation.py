def convertToBinaryData(filename):
    if not isinstance(filename, str):
        raise TypeError
    # Convert digital data to binary format
    with open(filename, "rb") as file:
        blobData = file.read()
    return blobData
