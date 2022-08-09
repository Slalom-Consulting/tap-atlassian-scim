"""Stream type classes for tap-atlassian-scim."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_atlassian_scim.client import atlassianScimStream

class UsersStream(atlassianScimStream):
    """Users stream"""
    name = "users"
    path = "/Users"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
#        th.Property(
#            "schemas",
#            th.ArrayType(th.StringType),
#            description="SCIM schemas that define the attributes present in the current JSON structure. This field is required during user creation or modification."
#        ),
        th.Property(
            "userName",
            th.StringType,
            description="Unique identifier defined by the provisioning client. Atlassian SCIM service will verify the value and guarantee its uniqueness."
        ),
        th.Property(
            "emails",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "value",
                        th.StringType,
                        description="Email address."
                    ),
                    th.Property(
                        "type",
                        th.StringType,
                        description='Type of email address, for example "work" or "personal".'
                    ),
                    th.Property(
                        "primary",
                        th.BooleanType,
                        description="Boolean value indicating whether this is the primary email address."
                    ),
                )
            ),
            description="Email addresses for the User. One value is marked as primary."
        ),
        th.Property(
            "id",
            th.StringType,
            description="Unique identifier defined by Atlassian SCIM Service. CaseExact."
        ),
        th.Property(
            "externalId",
            th.StringType,
            description="Identifier defined by provisioning client. This field is case-sensitive. Uniqueness is controlled by client."
        ),
        th.Property(
            "name",
            th.ObjectType(
                th.Property(
                    "formatted",
                    th.StringType,
                    description="The full name, including all middle names, titles, and suffixes as appropriate, formatted for display."
                ),
                th.Property(
                    "familyName",
                    th.StringType,
                    description="The family name of the User."
                ),
                th.Property(
                    "givenName",
                    th.BooleanType,
                    description="The given name of the User."
                ),
                th.Property(
                    "middleName",
                    th.StringType,
                    description="The middle name(s) of the User."
                ),
                th.Property(
                    "honorificPrefix",
                    th.StringType,
                    description="The honorific prefix(es) of the User, or title in most Western languages."
                ),
                th.Property(
                    "honorificSuffix",
                    th.BooleanType,
                    description="The honorific suffix(es) of the User, or suffix in most Western languages."
                ),
            ),
            description="The components of the user's name."
        ),
        th.Property(
            "displayName",
            th.StringType,
            description="User display name."
        ),
        th.Property(
            "nickName",
            th.StringType,
            description="User nickname."
        ),
        th.Property(
            "title",
            th.StringType,
            description="User title."
        ),
        th.Property(
            "preferredLanguage",
            th.StringType,
            description="User preferred language."
        ),
        th.Property(
            "department",
            th.StringType,
            description="User department."
        ),
        th.Property(
            "organization",
            th.StringType,
            description="User organization."
        ),
        th.Property(
            "timezone",
            th.StringType,
            description='User timezone. e.g. "America/Los_Angeles".'
        ),
        th.Property(
            "phoneNumbers",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "value",
                        th.StringType,
                        description="Phone number."
                    ),
                    th.Property(
                        "type",
                        th.StringType,
                        description='Type of phone number, for example "work" or "personal".'
                    ),
                    th.Property(
                        "primary",
                        th.BooleanType,
                        description="Boolean value indicating whether phone number is primary."
                    ),
                )
            ),
            description="Phone numbers for the user."
        ),
        th.Property(
            "meta",
            th.ObjectType(
                th.Property(
                    "resourceType",
                    th.StringType,
                    description="The name of the resource type of the resource. This field is case-sensitive."
                ),
                th.Property(
                    "location",
                    th.StringType,
                    description="The URI of the resource being returned."
                ),
                th.Property(
                    "lastModified",
                    th.BooleanType,
                    description="The most recent DateTime that the details of this resource were updated."
                ),
                th.Property(
                    "created",
                    th.StringType,
                    description=""
                ),
            ),
            description="User metadata information."
        ),
        th.Property(
            "groups",
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
                        "$ref",
                        th.StringType
                    ),
                )
            ),
            description="SCIM groups user belongs to."
        ),
        th.Property(
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            th.ObjectType(
                th.Property(
                    "organization",
                    th.StringType,
                    description="Organization the user belongs to."
                ),
                th.Property(
                    "department",
                    th.StringType,
                    description="Department the user belongs to."
                ),
            ),
            description="Enterprise user information."
        ),
        th.Property(
            "urn:scim:schemas:extension:atlassian-external:1.0",
            th.ObjectType(
                th.Property(
                    "atlassianAccountId",
                    th.StringType
                ),
            ),
            description="Atlassian specific SCIM Extension."
        ),
        th.Property(
            "active",
            th.BooleanType,
            description="A Boolean value indicating the user's administrative status."
        ),
    ).to_dict()


class GroupsStream(atlassianScimStream):
    """Groups stream"""
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
