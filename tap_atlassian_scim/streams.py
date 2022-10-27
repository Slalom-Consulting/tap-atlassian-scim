"""Stream type classes for tap-atlassian-scim."""

from pathlib import Path
from tap_atlassian_scim.client import AtlassianScimStream

SCHEMAS_DIR = Path(__file__).parent / Path('./schemas')
class UsersStream(AtlassianScimStream):
    """Users stream"""
    name = "users"
    path = "/Users"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = f'{SCHEMAS_DIR}/users.json'

class GroupsStream(AtlassianScimStream):
    """Groups stream"""
    name = "groups"
    path = "/Groups"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = f'{SCHEMAS_DIR}/groups.json'
