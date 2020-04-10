def test_version():
    """Make sure the version is the same on PyPI and in __init__.py"""
    try:
        from importlib.metadata import version
    except ImportError:
        # Backport in Python 3.7 and earlier
        from importlib_metadata import version  # type: ignore
    from pyhgvs_lite import __version__

    assert version("pyhgvs-lite") == __version__
