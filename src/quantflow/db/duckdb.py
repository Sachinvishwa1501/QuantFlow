from __future__ import annotations

from pathlib import Path

import duckdb
from duckdb import DuckDBPyConnection

from quantflow.core.settings import get_settings


def create_duckdb_connection(
    path: Path | None = None,
    read_only: bool = False,
) -> DuckDBPyConnection:
    """Create a DuckDB connection for analytical workloads.

    Args:
        path: Optional database file path. Uses configured path when omitted.
        read_only: Whether to open the connection in read-only mode.

    Returns:
        A DuckDB connection object.
    """
    db_path = path or get_settings().duckdb_path
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path), read_only=read_only)
