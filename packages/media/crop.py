from typing import Tuple
import cv2

def crop_video(input_path: str, output_path: str, crop_area: Tuple[int, int, int, int]) -> None:
    """
    Crop the video to the specified area.

    Parameters:
    - input_path: Path to the input video file.
    - output_path: Path to save the cropped video file.
    - crop_area: A tuple (x, y, width, height) defining the crop area.
    """
    x, y, width, height = crop_area
    cap = cv2.VideoCapture(input_path)
    
    # Get the original video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Crop the frame
        cropped_frame = frame[y:y+height, x:x+width]
        out.write(cropped_frame)

    cap.release()
    out.release()