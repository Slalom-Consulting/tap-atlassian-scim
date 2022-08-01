"""atlassianScim tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_atlassian_scim.streams import (
    atlassianScimStream,
    UsersStream,
    GroupsStream,
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]


class TapAtlassianScim(Tap):
    """atlassian-scim tap class."""
    name = "tap-atlassian-scim"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The key to authenticate against the API service"
        ),
        th.Property(
            "directory_id",
            th.StringType,
            required=True,
            description="Directory ID for the SCIM thing"
        ),
        th.Property(
            "batch_size",
            th.IntegerType,
            description="The number of records to return in each API call (Max of 100)"
        ),
        th.Property(
            "user_agent",
            th.StringType,
            description="The user agent to present to the API"
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
