from typing import Dict, Any
import subprocess
import json

class FFProbe:
    @staticmethod
    def probe(file_path: str) -> Dict[str, Any]:
        command = [
            'ffprobe',
            '-v', 'error',
            '-show_format',
            '-show_streams',
            '-of', 'json',
            file_path
        ]
        
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"FFProbe error: {e.stderr.decode().strip()}") from e

    @staticmethod
    def validate_media(file_path: str) -> bool:
        try:
            probe_info = FFProbe.probe(file_path)
            return bool(probe_info)
        except RuntimeError:
            return False

    @staticmethod
    def get_duration(file_path: str) -> float:
        probe_info = FFProbe.probe(file_path)
        return float(probe_info['format']['duration']) if 'format' in probe_info and 'duration' in probe_info['format'] else 0.0

    @staticmethod
    def get_video_streams(file_path: str) -> Any:
        probe_info = FFProbe.probe(file_path)
        return [stream for stream in probe_info.get('streams', []) if stream['codec_type'] == 'video']