import math

def conv(input_size, kernel_size, stride, padding, pool_kernel_size, pool_stride):
    layer = math.floor((input_size - kernel_size + 2*(padding))/stride + 1)
    layer = math.floor((layer - pool_kernel_size)/pool_stride + 1)
    return layer

def de_conv(input_size, kernel_size, stride, padding):
    return stride*(input_size - 1) + kernel_size - 2*padding

print(conv(input_size=28, kernel_size=3, stride=1, padding=1, pool_kernel_size=2, pool_stride=1))
print(de_conv(input_size=16, kernel_size=2, stride=2, padding=2))