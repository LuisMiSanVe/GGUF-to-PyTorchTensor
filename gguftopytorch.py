from gguf import GGUFReader
import numpy as np
import torch

# Load GGUF Model
gguf_file = "llama-model.gguf"
reader = GGUFReader(gguf_file)

# Extract the Model's Weight
weights = {}
for tensor in reader.tensors:  # Get the tensors as ReaderTensor type
    tensor_name = tensor.name  # Extract tensor's name
    tensor_data = tensor.data  # Extract tensor's data
    weights[tensor_name] = np.array(tensor_data, dtype=np.float32)

# Save the Model's Weight in a .npy file
np.save("llama-weight.npy", weights)
print("Model's Weight extracted and saved as 'llama.weight.npy'.")

user_input = input("See details? (Y/N): ")
if user_input.lower() == 'y':
    # Print the Weight's Keys
    print("Weight's Avaliable Keys:", weights.keys())
    # Weight Structure
    if len(weights) > 0:
        print("Weight Type:", type(weights))
        print("Weight Shape:", weights.shape if isinstance(weights, np.ndarray) else "Is not an ndarray.")
        print("Weight Content:", weights)

# Convert NumPy array to PyTorch tensor
pytorch_tensor = torch.from_numpy(weights[tensor_name])
torch.save(pytorch_tensor, "PyTorchTensor.pt")
print("Weight converted to PyTorch Tensor and saved as 'PyTorchTensor.pt'.")

user_input = input("See details? (Y/N): ")
if user_input.lower() == 'y':
    print("PyTorch Tensor data:", pytorch_tensor)