"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests

from tap_atlassian_scim.tap import TapAtlassianScim
from tap_atlassian_scim.tests.mock.util import mock_api

SAMPLE_CONFIG = {
    "api_key": "SampleApiKey",
    "directory_id": "SampleDirectoryId",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    config = SAMPLE_CONFIG
    tests = get_standard_tap_tests(TapAtlassianScim, config=config)
    for test in tests:
        if test.__name__ in ("_test_stream_connections"):
            mock_api(test, config)
            continue

        test()
