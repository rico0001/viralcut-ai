import pytest
import subprocess
import os

def test_ffmpeg_render():
    input_video = "tests/media/test_video.mp4"  # Path to a sample input video
    output_video = "tests/media/output_video.mp4"
    expected_output_duration = 10  # Expected duration in seconds for the output video

    # Ensure the input video exists
    assert os.path.exists(input_video), "Input video does not exist."

    # Run the FFmpeg command to render the video
    command = [
        "ffmpeg",
        "-i", input_video,
        "-t", str(expected_output_duration),
        "-vf", "scale=1080:1920",  # Resize to vertical format
        "-c:v", "libx264",
        "-c:a", "aac",
        "-strict", "experimental",
        output_video
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if FFmpeg executed successfully
    assert result.returncode == 0, f"FFmpeg failed with error: {result.stderr.decode()}"

    # Verify the output video was created
    assert os.path.exists(output_video), "Output video was not created."

    # Check the duration of the output video
    ffprobe_command = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        output_video
    ]

    duration_result = subprocess.run(ffprobe_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output_duration = float(duration_result.stdout.decode().strip())

    assert output_duration <= expected_output_duration + 1, "Output video duration is not as expected."

    # Clean up the output video after the test
    os.remove(output_video)