from typing import List, Dict

def format_captions(captions: List[Dict[str, str]], style: str = "default") -> List[str]:
    formatted_captions = []
    for caption in captions:
        start_time = caption.get("start_time", "0:00")
        end_time = caption.get("end_time", "0:00")
        text = caption.get("text", "")
        formatted_captions.append(f"[{start_time} - {end_time}] {text}")
    return formatted_captions

def generate_caption_file(captions: List[Dict[str, str]], file_path: str) -> None:
    with open(file_path, 'w') as f:
        for caption in format_captions(captions):
            f.write(caption + "\n")

def validate_captions(captions: List[Dict[str, str]]) -> bool:
    for caption in captions:
        if "start_time" not in caption or "end_time" not in caption or "text" not in caption:
            return False
    return True

def add_caption(captions: List[Dict[str, str]], start_time: str, end_time: str, text: str) -> None:
    captions.append({"start_time": start_time, "end_time": end_time, "text": text})