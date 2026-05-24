# Emit message if CUDA is unavailable

if not cuda_available:
    print('CUDA is not available.')