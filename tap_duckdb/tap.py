"""DuckDB tap class."""

from __future__ import annotations

from singer_sdk import SQLTap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_duckdb.client import DuckDBConnector, DuckDBStream


class TapDuckDB(SQLTap):
    """DuckDB tap class."""

    name = "tap-duckdb"
    default_stream_class = DuckDBStream

    config_jsonschema = th.PropertiesList(
        th.Property(
            "database",
            th.StringType,
            required=True,
            secret=True,
        ),
    ).to_dict()


if __name__ == "__main__":
    TapDuckDB.cli()
