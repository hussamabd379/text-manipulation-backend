import json
class Utils:
    @staticmethod
    def isJSON(value):
        try:
            json.loads(value)
            return True
        except Exception as ex:
            return False
