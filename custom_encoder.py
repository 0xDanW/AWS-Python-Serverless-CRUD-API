import json
from decimal import Decimal


### Custom JSON encoder class that takes in and checks for decimal instances and convert into float
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)
