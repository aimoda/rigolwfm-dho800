"""Version generated from git commit count."""
import subprocess
import os
import json


def get_version():
    """Get version in format X.Y.COMMIT_COUNT."""
    try:
        # Load base version from version_base.json
        here = os.path.abspath(os.path.dirname(__file__))
        version_file = os.path.join(os.path.dirname(here), 'version_base.json')

        with open(version_file, 'r') as f:
            version_data = json.load(f)

        major = version_data.get('major', 0)
        minor = version_data.get('minor', 2)

        # Get commit count for patch version
        result = subprocess.run(
            ['git', 'rev-list', '--count', 'HEAD'],
            capture_output=True,
            text=True,
            check=True,
            cwd=os.path.dirname(here)
        )
        commit_count = result.stdout.strip()

        return f"{major}.{minor}.{commit_count}"
    except Exception:
        # Fallback version if git not available or version file missing
        return "0.2.0"


__version__ = get_version()
