> [See in spanish/Ver en español](https://github.com/LuisMiSanVe/GGUF-to-PyTorchTensor/blob/main/README.es.md)
# 💾 GGUF to PyTorch Tensor Script
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)]()

This Script takes a GGUF model and extracts it's Weight then converts it to NumPy and PyTorch Tensor.

## 📋 Prerequisites
First of all, you'll need a GGUF Model.\
You can get one at [HuggingFace](https://huggingface.co/) or use other programs as [LM Studio](https://lmstudio.ai/) to get a Model.

Then, make sure you have [Python](https://www.python.org/) installed and clone the .py Script of the repository.

## 🛠️ Setup
You can setup the process in two ways:
- Go to the *llama.cpp* and either [build](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md) or download the [compiled](https://github.com/ggerganov/llama.cpp/releases).\
  To build it, you'll need [CMAKE](https://cmake.org/), and in case you use a NVIDIA GPU and you want to use it, make sure you have the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) installed too.
  Follow the build guide that fits the best for your system.\
  Install the necessary dependencies with the following command in a CMD:
```
cd llama.cpp
pip install -r requirements.txt
```
Or if it fails or you're using a newer version of Python:
```
cd llama.cpp
py -m pip install -r requirements.txt
``` 
Then, place the Script and the GGUF Model in `llama.cpp\gguf-py\gguf` so it takes the *gguf library* reference necessary for the process.

- Just install these Python libraries in a CMD: torch, numpy, sentencepiece, pyyaml and gguf
```
pip install torch numpy sentencepiece pyyaml gguf
```
Or if it fails or you're using a newer version of Python:
```
py -m pip install torch numpy sentencepiece pyyaml gguf
``` 
Make sure the Script and the GGUF Model is in the same folder.
## 🚀 Project Usage Explanation
Run the Script `gguftopytorch.py` in the terminal using the `py` or `python` command in the CMD or in an IDE like *Visual Studio Code* with the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) to save GGUF Weigths to PyTorch Tensor.

## 📂 Files
If the Script runs succesfully, it will generate two files in the same folder:
- <b>llama-weight.npy</b>: NumPy file with the GGUF LlaMA Model's Weight stored. 
- <b>PyTorchTensor.pt</b>: PyTorch Tensor file with the NumPy converted into a Tensor.

## 💻 Technologies Used
- Programming Language: [Python](https://www.python.org/) (3.13.2)
- Libraries:
  - [torch](https://pypi.org/project/torch/) (2.6.0)
  - [numpy](https://numpy.org/) (2.2.0)
  - [sentencepiece](https://pypi.org/project/sentencepiece/) (0.2.0)
  - [pyyaml](https://pypi.org/project/PyYAML/) (6.0.2)
  - [gguf](https://pypi.org/project/gguf/) (0.14.0)
- Other:
  - [CMAKE](https://cmake.org/) (3.31.5)
  - [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) (12.8)
  - [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Recommended IDE: [VS Code](https://code.visualstudio.com/)
