"""Mock Config."""

from pathlib import Path

API_URL = "https://api.atlassian.com/scim/directory/{directory_id}"
MOCK_RESPONSE_DIR = Path(__file__).parent / Path("responses")

mocks = [
    {
        "type": "stream",  # "stream": "users",
        "url": API_URL + "/Users",
        "file": MOCK_RESPONSE_DIR.joinpath("users.json"),
    },
    {
        "type": "stream",  # "stream": "groups",
        "url": API_URL + "/Groups",
        "file": MOCK_RESPONSE_DIR.joinpath("groups.json"),
    },
]
