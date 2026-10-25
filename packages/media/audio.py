from pydub import AudioSegment
import os

def extract_audio_from_video(video_path: str, output_audio_path: str) -> None:
    audio = AudioSegment.from_file(video_path)
    audio.export(output_audio_path, format="wav")

def normalize_audio(audio_path: str, output_audio_path: str) -> None:
    audio = AudioSegment.from_file(audio_path)
    normalized_audio = audio.apply_gain(-audio.dBFS)
    normalized_audio.export(output_audio_path, format="wav")

def split_audio(audio_path: str, start_time: int, end_time: int, output_audio_path: str) -> None:
    audio = AudioSegment.from_file(audio_path)
    split_audio = audio[start_time:end_time]
    split_audio.export(output_audio_path, format="wav")

def get_audio_duration(audio_path: str) -> float:
    audio = AudioSegment.from_file(audio_path)
    return len(audio) / 1000.0  # duration in seconds

def convert_audio_format(input_audio_path: str, output_audio_path: str, format: str) -> None:
    audio = AudioSegment.from_file(input_audio_path)
    audio.export(output_audio_path, format=format)