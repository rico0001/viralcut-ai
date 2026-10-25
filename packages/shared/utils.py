def generate_unique_id():
    import uuid
    return str(uuid.uuid4())

def format_timestamp(timestamp):
    from datetime import datetime
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def validate_video_format(file_extension):
    allowed_formats = ['mp4', 'mov', 'avi', 'mkv']
    return file_extension.lower() in allowed_formats

def calculate_duration(start_time, end_time):
    return end_time - start_time if end_time > start_time else 0

def sanitize_filename(filename):
    import re
    return re.sub(r'[<>:"/\\|?*]', '_', filename)