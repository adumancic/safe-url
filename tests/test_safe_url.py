import pytest
from safe_url import is_safe


@pytest.mark.parametrize("url", [
    "https://example.com",
    "http://example.com:8080/path?q=1",
    "https://8.8.8.8/",
])
def test_public_urls_are_safe(url):
    assert is_safe(url)


@pytest.mark.parametrize("url", [
    "http://localhost/",
    "http://127.0.0.1:8080/admin",
    "http://10.0.0.5/",
    "http://192.168.1.1/",
    "http://169.254.169.254/latest/meta-data/",
    "http://[::1]/",
    "file:///etc/passwd",
    "gopher://example.com/",
])
def test_internal_urls_are_blocked(url):
    assert not is_safe(url)


def test_custom_schemes():
    assert not is_safe("http://example.com", allowed_schemes={"https"})
