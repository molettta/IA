import cv2
import os

def extract_frames(video_path, output_folder, frame_skip=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_capture = cv2.VideoCapture(video_path)
    success, frame = video_capture.read()
    frame_count = 0

    while success:
        if frame_count % frame_skip == 0:
            output_path = os.path.join(output_folder, f"{frame_count/frame_skip}.jpg")
            cv2.imwrite(output_path, frame)
        success, frame = video_capture.read()
        frame_count += 1

    video_capture.release()
    print(f"Frames extraídos e salvos em {output_folder}")

# Exemplo de uso
for nomes in os.listdir('videos_test'):
    video_patch = os.path.join('videos_test', nomes)
    extract_frames(video_patch, f'frames_test/{nomes}', frame_skip=3)
