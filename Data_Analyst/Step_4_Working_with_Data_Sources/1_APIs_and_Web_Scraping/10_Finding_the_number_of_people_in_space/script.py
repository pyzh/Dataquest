# Generated by Haxe 3.3.0

import requests as Requests


class Script:
    __slots__ = ()

    @staticmethod
    def main():
        response = Requests.get("http://api.open-notify.org/astros.json")
        response_object = response.json()
        in_space_count = response_object["number"]
        print(str(in_space_count))



Script.main()