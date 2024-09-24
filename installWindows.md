
# Orientação para instalação no Windows
## Abaixo se encontra um passo a passo de como realizar a instalação do programa no Windows


### Requisitos 

- Windows 10 (ou superior)
- Python versão 3 (ou superior)
- Git

### Passos 
**1.** Baixar e instalar o Git
```bash
```
**2.**  Baixar e instalar o Python
```bash
 Abra o Windows PowerShell e insira a seguinte linha:
 sudo apt-get install python3.9
```
 **3.** Clone o projeto no diretório que desejar
 ````bash
 git clone https://github.com/molettta/IA.git
 ````
**4.** Extrair **Frames** do vídeo:

- Use o script `video2frame.py` para extrair os frames do vídeo em questão.

**5.**  Detecção de Faces:

- Execute o script `frame2face.py` para detectar rostos em cada frame extraído.

**6.**  Processamento de Faces:

- Use o `face2proc.py` para processar as faces detectadas.

**7.**  Treinamento e Teste:

- Execute o script `treinaEtesta.py` para treinar o modelo de IA e testar os resultados.

**8.**  Testes:

- Realize testes finais usando `teste2.py` para garantir que tudo está funcionando corretamente.
