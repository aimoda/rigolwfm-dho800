"""Version information for rigolwfm-dho800."""

try:
    from importlib.metadata import version
    __version__ = version("rigolwfm-dho800")
except Exception:
    # Fallback for development installations
    __version__ = "0.0.0.dev0"
