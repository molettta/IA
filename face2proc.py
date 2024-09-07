import cv2  # módulo do OpenCV, uma biblioteca poderosa para processamento de imagens e visão computacional. Usada para ler, redimensionar e salvar as imagens.
import os   # módulo da biblioteca padrão do Python, permite interagir com o sistema de arquivos (para navegar entre pastas, verificar existência de diretórios, etc.).

#Esta função recebe três parâmetros:
#faces_folder: O caminho da pasta onde estão armazenadas as imagens faciais que serão processadas.
#output_folder: O caminho onde as imagens redimensionadas serão salvas.
#size: O tamanho para o qual as imagens serão redimensionadas

def preprocess_faces(faces_folder, output_folder, size=(224, 224)):


#Se a pasta de saída (output_folder) não existir, ela será criada com os.makedirs().
#Isso garante que o script não falhe ao tentar salvar as imagens redimensionadas.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

#O código percorre cada arquivo da pasta de faces (faces_folder), lê cada imagem usando cv2.imread(), 
# redimensiona com cv2.resize() para o tamanho especificado e salva a imagem redimensionada na pasta de saída usando cv2.imwrite()

    for face_image_name in os.listdir(faces_folder):
        face_image_path = os.path.join(faces_folder, face_image_name)
        face_image = cv2.imread(face_image_path)
        resized_face_image = cv2.resize(face_image, size)
        output_path = os.path.join(output_folder, face_image_name)
        cv2.imwrite(output_path, resized_face_image)

#Exibe mensagem confirmando que as imagens foram pré-processadas e salvas na pasta de destino
    print(f"Imagens pré-processadas e salvas em {output_folder}")

# Exemplo de uso
#Esse trecho percorre uma pasta chamada 'faces_test', onde aparentemente existem subpastas com imagens faciais.
#Para cada subpasta, ele aplica a função preprocess_faces, salvando as imagens processadas
#  em uma pasta de saída ('processado_test/{nomes}'), redimensionadas para 128x128 pixels.

for nomes in os.listdir('faces_test'):
    pasta_de_frame_patch = os.path.join('faces_test', nomes)
    preprocess_faces(pasta_de_frame_patch, f'processado_test/{nomes}', size=(128, 128))
