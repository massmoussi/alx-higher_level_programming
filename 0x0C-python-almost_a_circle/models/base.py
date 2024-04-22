#!/usr/bin/python3

"""Define Our Base Class """
import json


class Base:
    """
    Insatiate private Class attribute nb_object to 0
    Verify if id is not None to assign id value to self.id
    if it fail increment nb_object assign the value to self.id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        list_dicts = []
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    dict_obj = obj.to_dictionary()
                    list_dicts.append(dict_obj)
                json_str = cls.to_json_string(list_dicts)
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)

            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
