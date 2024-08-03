
import torch


def CUDA_Avail():
    return torch.cuda.is_available()
