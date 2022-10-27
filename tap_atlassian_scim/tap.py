"""atlassianScim tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_atlassian_scim.streams import (
    UsersStream,
    GroupsStream,
)

STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]

class TapAtlassianScim(Tap):
    """atlassian-scim tap class."""
    name = "tap-atlassian-scim"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "directory_api_key",
            th.StringType,
            required=True,
            description="API key for SCIM directory authentication"
        ),
        th.Property(
            "directory_id",
            th.UUIDType,
            required=True,
            description="ID of the SCIM directory"
        ),
        th.Property(
            "batch_size",
            th.IntegerType,
            description="Number of results returned per page (Default: 100, Max: 100)"
        ),
        th.Property(
            "user_agent",
            th.StringType,
            description="User agent to present to the API"
        ),
        th.Property(
            'api_url',
            th.StringType,
            default='https://api.atlassian.com',
            description='API URL'
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
