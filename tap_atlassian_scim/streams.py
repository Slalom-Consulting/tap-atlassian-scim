"""Stream type classes for tap-atlassian-scim."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_atlassian_scim.client import atlassianScimStream

# TODO: Delete this is if not using json files for schema definition
# SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# class UsersStream(atlassianScimStream):
#     """Define custom stream."""
#     name = "users"
#     path = "/Users"
#     primary_keys = ["id"]
#     replication_key = None
#     # Optionally, you may also use `schema_filepath` in place of `schema`:
#     # schema_filepath = SCHEMAS_DIR / "users.json"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property(
#             "id",
#             th.StringType,
#             description="The user's system ID"
#         ),
#         th.Property(
#             "age",
#             th.IntegerType,
#             description="The user's age in years"
#         ),
#         th.Property(
#             "email",
#             th.StringType,
#             description="The user's email address"
#         ),
#         th.Property("street", th.StringType),
#         th.Property("city", th.StringType),
#         th.Property(
#             "state",
#             th.StringType,
#             description="State name in ISO 3166-2 format"
#         ),
#         th.Property("zip", th.StringType),
#     ).to_dict()


class GroupsStream(atlassianScimStream):
    """Define custom stream."""
    name = "groups"
    path = "/Groups"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
#        th.Property(
#            "schemas",
#            th.ArrayType(th.StringType),
#            description="SCIM schemas that define the attributes present in the current JSON structure. This field is required during user creation or modification."
#        ),
        th.Property(
            "id",
            th.StringType,
            description="Unique identifier defined by Atlassian SCIM Service. This field is read-only and case-sensitive. It is ignored if specified in the payload during user creation or modification."
        ),
        th.Property(
            "externalId",
            th.StringType,
            description="Identifier defined by provisioning client. CaseExact. Uniqueness is controlled by client."
        ),
        th.Property(
            "displayName",
            th.StringType,
            description="Group display name. This field is immutable, required, and read-only."
        ),
        th.Property(
            "members",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "type",
                        th.StringType
                    ),
                    th.Property(
                        "value",
                        th.StringType
                    ),
                    th.Property(
                        "display",
                        th.StringType
                    ),
                    th.Property(
                        "created",
                        th.StringType
                    ),
                )
            ),
            description="Group members"
        ),
        th.Property(
            "meta",
            th.ObjectType(
                th.Property(
                    "resourceType",
                    th.StringType,
                    description="The name of the resource type of the resource. This field is read-only and case-sensitive."
                ),
                th.Property(
                    "location",
                    th.StringType,
                    description="The URI of the resource being returned. This field is read-only."
                ),
                th.Property(
                    "lastModified",
                    th.StringType,
                    description="The most recent DateTime that the details of this resource were updated. This field is read-only."
                ),
                th.Property(
                    "created",
                    th.StringType,
                    description="The DateTime that the resource was added to Atlassian SCIM service. This field is read-only."
                ),
            ),
            description="Group metadata information."
        ),
    ).to_dict()