import torch



# Scalar (0-D tensor)
# A scalar is a single number. It is a tensor represnted with no dimensions.
scalar = torch.tensor(42)
print(scalar)
print(scalar.shape)
print(scalar.dim())

# Vector (1-D tensor)
# A vector is a one-dimensional array of numbers
vector = torch.tensor([1, 2, 3, 4, 5])
print(vector)
print(vector.shape)
print(vector.dim())


# 3-D tensor
# It is a three dimensional array of numbers
tensor_3d = torch.tensor([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor_3d)
print(tensor_3d.shape)
print(tensor_3d.dim())

# Higher-Dimensional Tensors
# Tensors can have more than 3 dimensions.
tensor_4d = torch.rand(2,3,4,5)
print(tensor_4d)
print(tensor_4d.shape)
print(tensor_4d.dim())