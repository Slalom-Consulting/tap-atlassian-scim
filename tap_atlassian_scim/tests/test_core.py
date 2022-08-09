"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_atlassian_scim.tap import TapAtlassianScim

SAMPLE_CONFIG = {
    "directory_api_key": "abcdABCD1234",
    "directory_id": "00000000-00000000-00000000-00000000",
    "batch_size": 100,
    "user_agent": "singer tap",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapAtlassianScim,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
