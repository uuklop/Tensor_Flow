import torch



# Scalar (0-D tensor)
# A scalar is a single number. It is a tensor represnted with no dimensions.
scalar = torch.tensor(42)
print(scalar)
print(scalar.shape)
print(scalar.dim())