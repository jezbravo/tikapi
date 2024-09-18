from tikapi import TikAPI, ValidationException, ResponseException
import json
import os


api = TikAPI(os.getenv("API_KEY"))


def user_profile_info(username):
    try:
        response = api.public.check(username)
        data = response.json()
        readable_data = json.dumps(data, indent=4)

        print(readable_data)

        with open("user_profile_info.txt", "w") as file:
            file.write(readable_data)

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)


def discover_by_keyword(keyword):
    try:
        response = api.public.discoverKeyword(keyword)
        data = response.json()
        readable_data = json.dumps(data, indent=4)

        print(readable_data)

        with open("discover_by_keyword.txt", "w") as file:
            file.write(readable_data)

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)


def get_video_information(id):
    try:
        response = api.public.video(id)
        data = response.json()
        readable_data = json.dumps(data, indent=4)

        print(readable_data)

        with open("get_video_information.txt", "w") as file:
            file.write(readable_data)

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)


user_profile_info("ebravo_abs")

# discover_by_keyword("catvideos") <- not working

get_video_information("7409089170519395626")
