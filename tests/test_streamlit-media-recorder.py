"""Package related tests."""
from streamlit-media-recorder import __version__


def test_streamlit-media-recorder_version():
    """Checks correct package version."""
    assert __version__ == "0.1.0"
