"""safe-url: block URLs that point at internal infrastructure."""

import ipaddress
from urllib.parse import urlparse

__version__ = "0.3.1"
__all__ = ["is_safe"]

DEFAULT_SCHEMES = frozenset({"http", "https"})
BLOCKED_HOSTNAMES = frozenset({"localhost", "localhost.localdomain"})


def _is_internal_ip(host: str) -> bool:
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False  # not an IP literal -> treat as a domain name
    return ip.is_loopback or ip.is_private or ip.is_link_local or ip.is_reserved


def is_safe(url: str, allowed_schemes=DEFAULT_SCHEMES) -> bool:
    """Return True if ``url`` is safe for the server to fetch."""
    parsed = urlparse(url)
    if parsed.scheme not in allowed_schemes:
        return False

    host = (parsed.hostname or "").lower()
    if not host or host in BLOCKED_HOSTNAMES:
        return False

    _ = parsed.port  # validate port
    return not _is_internal_ip(host)
