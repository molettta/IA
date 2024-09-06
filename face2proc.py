import cv2
import os

def preprocess_faces(faces_folder, output_folder, size=(224, 224)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for face_image_name in os.listdir(faces_folder):
        face_image_path = os.path.join(faces_folder, face_image_name)
        face_image = cv2.imread(face_image_path)
        resized_face_image = cv2.resize(face_image, size)
        output_path = os.path.join(output_folder, face_image_name)
        cv2.imwrite(output_path, resized_face_image)

    print(f"Imagens pré-processadas e salvas em {output_folder}")

# Exemplo de uso
for nomes in os.listdir('faces_test'):
    pasta_de_frame_patch = os.path.join('faces_test', nomes)
    preprocess_faces(pasta_de_frame_patch, f'processado_test/{nomes}', size=(128, 128))
