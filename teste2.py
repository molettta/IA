import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Diretório das imagens de teste e carregamento do modelo
test_dir = 'processadoTest'
model = load_model('modelos/modelo1.h5')

# Tamanho das imagens usadas no modelo
img_size = (128 , 128)  # ou o tamanho que você utilizou

# Defina manualmente os rótulos das classes conforme o que foi usado no treinamento
class_labels = sorted(os.listdir(test_dir))  # Ajuste conforme o seu conjunto de dados
print(class_labels)

# Carregar imagens da pasta de teste
test_images = []
test_labels = []
image_paths = []
for label in os.listdir(test_dir):
    label_dir = os.path.join(test_dir, label)
    for image_file in os.listdir(label_dir):
        img_path = os.path.join(label_dir, image_file)
        image = load_img(img_path, target_size=img_size)
        image = img_to_array(image) / 255.0  # Normalização
        test_images.append(image)
        test_labels.append(label)
        image_paths.append(img_path)

# Converter para numpy arrays
test_images = np.array(test_images)

# Fazer as predições
predictions = model.predict(test_images)

# Mapeamento de índices para nomes de classes
class_indices = {v: k for k, v in {0: class_labels[0], 1: class_labels[1], 2: class_labels[2], 3: class_labels[3], 4: class_labels[4], 5: class_labels[5], 6: class_labels[6], 7: class_labels[7], 8: class_labels[8], 9: class_labels[9], 10: class_labels[10], 11: class_labels[11], 12: class_labels[12], 13: class_labels[13]}.items()}  # Ajuste de acordo com seu dataset

# Exibir as imagens com as predições
plt.figure(figsize=(15, 15))
class_counts = {i: 0 for i in range(len(class_indices))}  # Contadores de cada classe

for i in range(len(test_images)):  # Mostrar todas as imagens
    pred_index = np.argmax(predictions[i])
    true_label = test_labels[i]
    predicted_label = class_labels[pred_index]
    
    ax = plt.subplot(6, 6, i+1)
    plt.imshow(test_images[i])
    plt.title(f"Verdadeiro: {true_label}\nPredito: {predicted_label}")
    plt.axis("off")
    class_counts[pred_index] += 1

print(len(test_images))
plt.tight_layout()
plt.savefig('plot.png')  # Salvar o gráfico como imagem
plt.close()  # Fechar a figura para liberar memória