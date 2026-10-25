from typing import Dict, Any
import subprocess
import json

def probe_media(file_path: str) -> Dict[str, Any]:
    """
    Probes the media file using FFprobe and returns metadata.

    Args:
        file_path (str): The path to the media file.

    Returns:
        Dict[str, Any]: A dictionary containing the media metadata.
    """
    try:
        # Run FFprobe command to get media information
        command = [
            'ffprobe',
            '-v', 'error',
            '-show_format',
            '-show_streams',
            '-of', 'json',
            file_path
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            raise Exception(f"FFprobe error: {result.stderr.strip()}")

        # Parse the JSON output
        metadata = json.loads(result.stdout)
        return metadata

    except Exception as e:
        raise RuntimeError(f"Failed to probe media file: {str(e)}")