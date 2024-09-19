# Orientação para instalação no linux (Ubuntu)
## Abaixo se encontra um passo a passo de como realizar a instalação do programa no linux 


### Requisitos 

- Linux Ubuntu versão 22.0.4 ou superior
- Python 3.x

### Passos 
**1.** Clone o projeto no diretório que desejar
```bash
git clone https://github.com/molettta/IA.git
```
 **2.** Instalar o Python 
 ````bash
 sudo apt-get install python3.9
 ````
**3.** Converter Vídeo em Frames:

- Use o script `video2frame.py` para converter os vídeos em frames.

**4.**  Detecção de Faces:

- Execute o script `frame2face.py` para detectar rostos em cada frame extraído.

**5.**  Processamento de Faces:

- Use o `face2proc.py` para processar as faces detectadas.

**6.**  Treinamento e Teste:

- Execute o script `treinaEtesta.py` para treinar o modelo de IA e testar os resultados.

**7.**  Testes:

- Realize testes finais usando `teste2.py` para garantir que tudo está funcionando corretamente.


