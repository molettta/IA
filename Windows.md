# 🎯 Projeto de Rede Neural para Reconhecimento Facial

## 📜 Visão Geral
Este projeto realiza reconhecimento facial utilizando uma rede neural. O pipeline envolve a extração de quadros de vídeos, detecção de rostos e classificação usando um modelo pré-treinado.

## 📁 Estrutura do Projeto
- [`face2proc.py`](./face2proc.py): Pré-processa as imagens de rostos.
- [`frame2face.py`](./frame2face.py): Detecta rostos em quadros de vídeos.
- [`teste2.py`](./teste2.py): Classifica as imagens processadas com um modelo.
- [`video2frame.py`](./video2frame.py): Extrai quadros de vídeos.

## 🛠️ Requisitos
- Python 3.x
- OpenCV
- face_recognition
- TensorFlow/Keras
- Matplotlib
- NumPy

Você pode instalar as dependências necessárias executando:
```bash
pip install -r requirements.txt
```

### 🪟 Instalação no Windows
1. **Instale o Python 3.x**: Baixe e instale a versão mais recente em [python.org](https://www.python.org/downloads/). Marque "Add Python to PATH".
2. **Instale as bibliotecas**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Usar

### 1. 📽️ Extração de Quadros de Vídeos
Use o script [`video2frame.py`](./video2frame.py) para extrair quadros de um vídeo:
```bash
python video2frame.py <caminho_do_video> <pasta_saida> [frames_a_pular]
```

### 2. 🕵️ Detecção de Rostos
Execute o script [`frame2face.py`](./frame2face.py) para detectar rostos nos quadros:
```bash
python frame2face.py <pasta_quadros> <pasta_saida>
```

### 3. 🧑‍🔬 Pré-processamento dos Rostos
Pré-processe os rostos detectados usando o [`face2proc.py`](./face2proc.py):
```bash
python face2proc.py <pasta_faces> <pasta_saida> [tamanho]
```

### 4. 🧠 Classificação dos Rostos
Depois que os rostos forem pré-processados, execute o [`teste2.py`](./teste2.py) para classificá-los:
```bash
python teste2.py
```

## 🔧 Problemas com dlib?
Se ocorrerem problemas ao compilar o dlib, use uma versão pré-compilada. No Windows, tente baixar em [dlib releases](https://github.com/davisking/dlib/releases), ou use o comando:
```bash
pip install dlib==19.8.1 --find-links <url>
```

## 🤝 Contribuição
Sinta-se à vontade para fazer um fork deste repositório, abrir issues e enviar pull requests.

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.

Agora, os arquivos estão com links clicáveis que redirecionam diretamente para eles, facilitando a navegação no repositório. Isso melhora a usabilidade do README, tornando-o mais prático para quem está seguindo os passos do projeto.