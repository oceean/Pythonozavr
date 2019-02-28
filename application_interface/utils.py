import json
from datetime import datetime

def no_datetime(data) -> dict:
    if type(data) == dict:
        for key, value in data.items():
            data[key] = no_datetime(value)
        return data
    elif type(data) == list:
        newdata = []
        for value in data:
            newdata.append(no_datetime(value))
        return newdata
    else:
        if type(data) == datetime:
            return data.timestamp()
        else:
            return data

def js_in(data):
    return json.loads(data)

def js_out(data):
    return json.dumps(no_datetime(data), ensure_ascii=False)