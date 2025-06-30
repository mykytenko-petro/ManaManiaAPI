from bson.objectid import ObjectId

def parse(data : list[dict]) -> list:
    for data_dict in data:
        for key, value in data_dict.items():
            if isinstance(value, ObjectId):
                data_dict[key] = str(value)

    return data