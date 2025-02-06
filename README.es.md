> [Ver en ingles/See in english](https://github.com/LuisMiSanVe/GGUF-to-PyTorchTensor/blob/main/README.md)
# 💾 Script de GGUF a PyTorch Tensor
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

Este Script coge un Modelo GGUF y extrae su Peso para convertirlo en NumPy y PyTorch Tensor.

## 📋 Prerequisitos
Antes de nada, necesitas el Modelo GGUF.\
Puedes conseguir uno en [HuggingFace](https://huggingface.co/) o usando otros programas como [LM Studio](https://lmstudio.ai/) para conseguir un modelo.

Tambien, asegurate que tienes [Python](https://www.python.org/) instalado y clona el Script .py del repositorio.

## 🛠️ Instalación
Puedes preparar el proceso de dos formas:
- Ve al repositorio de *llama.cpp* y [compila](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md) o descargalo ya [compilado](https://github.com/ggerganov/llama.cpp/releases).\
  Para compilarlo, necesitarás [CMAKE](https://cmake.org/), y en caso que tengas una GPU de Nvidia y quieres usarla, asegurate de tener instalado tambien el [Toolkit de CUDA](https://developer.nvidia.com/cuda-toolkit).
  Sigue la guia de compilacion que se adecue más a tu sistema.\
  Instala las dependencias necesarias con el siguiente comando en el CMD:
```
cd llama.cpp
pip install -r requirements.txt
```
O si te falla o tienes una versión más nueva de Python:
```
cd llama.cpp
py -m pip install -r requirements.txt
``` 
Entonces, deja el Script y el modelo GGUF en `llama.cpp\gguf-py\gguf` para que encuentre la referencia de la *librería de gguf* necesaria para el proceso.

- Simplemente instala estas librerias de Python en el CMD: torch, numpy, sentencepiece, pyyaml y gguf
```
pip install torch numpy sentencepiece pyyaml gguf
```
O si te falla o tienes una versión más nueva de Python:
```
py -m pip install torch numpy sentencepiece pyyaml gguf
``` 
Asegurate que el Script y el modelo GGUF están en la misma carpeta.
## 🚀 Explicación de uso del proyecto
Ejecuta el Script `gguftopytorch.py` en un terminal usando el comando `py` o `python` o en un IDE como *Visual Studio Code* con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) para guardar el Peso de GGUF a PyTorch Tensor.

## 📂 Archivos
Si el Script se ejecuta correctamente, aparecerán dos nuevos archivos en esa carpeta:
- <b>llama-weight.npy</b>: Archivo de NumPy con el Peso del Modelo GGUF de LlaMA guardado. 
- <b>PyTorchTensor.pt</b>: Archivo de PyTorch Tensor con el NumPy convertido en Tensor.

## 💻 Tecnologías usadas
- Lenguaje de programación: [Python](https://www.python.org/) (3.13.2)
- Librerias:
  - [torch](https://pypi.org/project/torch/) (2.6.0)
  - [numpy](https://numpy.org/) (2.2.0)
  - [sentencepiece](https://pypi.org/project/sentencepiece/) (0.2.0)
  - [pyyaml](https://pypi.org/project/PyYAML/) (6.0.2)
  - [gguf](https://pypi.org/project/gguf/) (0.14.0)
- Otro:
  - [CMAKE](https://cmake.org/) (3.31.5)
  - [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) (12.8)
  - [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- IDE Recomendado: [VS Code](https://code.visualstudio.com/)
