from subprocess import Popen, PIPE
import os

class FFmpeg:
    @staticmethod
    def run_command(command):
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        return stdout, stderr, process.returncode

    @staticmethod
    def render_video(input_file, output_file, start_time, duration, caption_file=None):
        command = [
            'ffmpeg',
            '-i', input_file,
            '-ss', str(start_time),
            '-t', str(duration),
            '-vf', 'subtitles=' + caption_file if caption_file else '',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_file
        ]
        return FFmpeg.run_command(command)

    @staticmethod
    def extract_audio(input_file, output_file):
        command = [
            'ffmpeg',
            '-i', input_file,
            '-q:a', '0',
            '-map', 'a',
            output_file
        ]
        return FFmpeg.run_command(command)

    @staticmethod
    def get_metadata(input_file):
        command = [
            'ffprobe',
            '-v', 'error',
            '-show_format',
            '-show_streams',
            input_file
        ]
        return FFmpeg.run_command(command)