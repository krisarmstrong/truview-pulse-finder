"""Automation sessions for truview-pulse-finder."""

from __future__ import annotations

import nox

nox.options.sessions = ["tests"]


@nox.session
def tests(session: nox.Session) -> None:
    """Run the test suite under the active interpreter."""
    session.install("-e", ".")
    session.install("pytest", "pytest-cov", "websockets")
    session.run("pytest", "--cov=BigRedWebSocketClient", "--cov-report=term-missing")
