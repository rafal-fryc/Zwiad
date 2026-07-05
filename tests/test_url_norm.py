import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.url_norm import normalize_url


def test_utm_first_param_does_not_mangle_url():
    assert normalize_url("https://x.com/a?utm_source=n&id=5") == "https://x.com/a?id=5"


def test_param_order_insensitive_for_stripping():
    a = normalize_url("https://x.com/a?utm_source=n&id=5")
    b = normalize_url("https://x.com/a?id=5&utm_source=n")
    assert a == b == "https://x.com/a?id=5"


def test_forces_https_and_strips_trailing_slash():
    assert normalize_url("http://example.com/foo/") == "https://example.com/foo"


def test_lexology_g_param_stripped():
    assert normalize_url("https://www.lexology.com/library/detail.aspx?g=abc123") == \
        "https://lexology.com/library/detail.aspx"


def test_host_lowercased_www_stripped_fragment_dropped():
    assert normalize_url("https://WWW.Example.com/Path#frag") == "https://example.com/Path"


def test_empty_and_whitespace():
    assert normalize_url("") == ""
    assert normalize_url("  https://a.com  ") == "https://a.com"


def test_non_http_garbage_passthrough():
    # No scheme: returned trimmed but untouched otherwise
    assert normalize_url("not a url") == "not a url"
