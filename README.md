# tap-atlassian-scim

`tap-atlassian-scim` is a Singer tap for the [Atlassian user provisioning REST API (SCIM)](https://developer.atlassian.com/cloud/admin/user-provisioning/about/).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps and the [Atlassian user provisioning REST API Reference](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/intro/)

<!--

Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-atlassian-scim
```

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-atlassian-scim.git@main
```

-->

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-atlassian-scim --about --format=markdown
```
-->
## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| api_key             | True     | None    | API key for SCIM directory authentication. |
| directory_id        | True     | None    | ID of the SCIM directory. |
| limit               | False    |     100 | Number of results returned per page. (Max: 100) |
| user_agent          | False    | None    | User agent to present to the API. |
| api_url             | False    | None    | Override the Atlassian API base URL. |
| stream_config       | False    | None    | A list of dictionaries for specifing addtional configurations for a specified stream |

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-atlassian-scim --about
```

### Settings for Specific Streams

Settings can be added on a per stream basis and can be set using the stream_config setting. The stream_config setting takes a list of dictionaries, requiring the stream name as a value in the stream key. If the same stream name is added multilpe times, only the last will be used.

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| stream              | True     | None    | Name of the stream to configure |
| parameters          | False    | None    | URL query string to send to the stream endpoint |

Example:

```json
{
    "stream_config": [
        {
            "stream": "STREAM_NAME",
            "parameters": "URL_QUERY_STRING"
        }
    ]
}
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

Required auth configuration can be found [here](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/).

### Executing the Tap Directly

```bash
tap-atlassian-scim --version
tap-atlassian-scim --help
tap-atlassian-scim --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_atlassian_scim/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap_atlassian_scim` CLI interface directly using `poetry run`:

```bash
poetry run tap-atlassian-scim --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-atlassian-scim
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-atlassian-scim --version
# OR run a test `elt` pipeline:
meltano elt tap-atlassian-scim target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
