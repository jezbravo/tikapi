# **TikAPI Test App**

## Introduction

This is a Python application that utilizes the TikAPI library to interact with the TikTok API. The app provides three functions to retrieve information from TikTok:

### Functions

#### 1. `user_profile_info(username)`

- Retrieves profile information for a given TikTok username.
- Saves the response data to a file named `user_profile_info.txt` in a readable JSON format.

#### 2. `discover_by_keyword(keyword)`

- Searches for TikTok content using a given keyword.
- Saves the response data to a file named `discover_by_keyword.txt` in a readable JSON format.

#### 3. `get_video_information(id)`

- Retrieves information about a specific TikTok video using its ID.
- Saves the response data to a file named `get_video_information.txt` in a readable JSON format.

### Usage

To use the app, simply run the `app.py` script and pass in the required parameters for each function. For example:

- `user_profile_info("ebravo_abs")` to retrieve profile information for the user "ebravo_abs".
- `get_video_information("7409089170519395626")` to retrieve information about a video with the ID "7409089170519395626".

**Note:** The `discover_by_keyword` function is currently not working as intended. Further development is required to resolve this issue.

### Dependencies

- `tikapi` library: used to interact with the TikTok API.
- `os` library: used to retrieve environment variables.
- `json` library: used to format JSON data in a readable manner.

### Environment Variables

The app requires an `API_KEY` environment variable to be set, which is used to authenticate requests to the TikTok API.

### Error Handling

The app catches and prints `ValidationException` and `ResponseException` errors, which may occur during API requests.

### Output

The app saves response data to text files in the same directory as the script, with file names indicating the type of data retrieved. The data is formatted in a readable JSON format using indentation.
