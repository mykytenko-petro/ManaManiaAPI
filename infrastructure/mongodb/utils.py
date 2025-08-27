from bson.objectid import ObjectId


def parse(data : list[dict]) -> list[dict]:
    for data_dict in data:
        for key, value in data_dict.items():
            if isinstance(value, ObjectId):
                data_dict[key] = str(object=value)

    return data

def dump(data : dict) -> dict:
    for key, value in data.items():
        if key == "_id":
            data[key] = ObjectId(oid=value)

    return data