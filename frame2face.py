import face_recognition
import os
import cv2

def detect_faces_in_frames(frames_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image_name in os.listdir(frames_folder):
        image_path = os.path.join(frames_folder, image_name)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        for face_count, (top, right, bottom, left) in enumerate(face_locations):
            face_image = image[top:bottom, left:right]
            face_image_path = os.path.join(output_folder, f"{image_name}_face{face_count}.jpg")
            cv2.imwrite(face_image_path, face_image[:, :, ::-1])

    print(f"Rostos detectados e salvos em {output_folder}")

# Exemplo de uso
for nomes in os.listdir('frames_test'):
    pasta_de_frame_patch = os.path.join('frames_test', nomes)
    detect_faces_in_frames(pasta_de_frame_patch, f'faces_test/{nomes}')
