# safe-url

Tiny, dependency-free URL validation for Python — stop your server from fetching
URLs that point at `localhost`, private networks or cloud metadata endpoints.

```python
from safe_url import is_safe

is_safe("https://example.com/image.png")   # True
is_safe("http://127.0.0.1:8080/admin")      # False
is_safe("http://169.254.169.254/latest/")  # False
```

## Install

```bash
pip install safe-url
```

## What it blocks

- Non-HTTP(S) schemes (`file://`, `gopher://`, `ftp://`, ...)
- Loopback addresses (`127.0.0.0/8`, `::1`, `localhost`)
- Private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`)
- Link-local / cloud metadata (`169.254.0.0/16`)

## Configuration

```python
is_safe(url, allowed_schemes={"https"})
```

## Contributing

Issues and PRs welcome! Run the tests with `pytest`.

## License

MIT
