#Feed Forward

import torch

x= torch.tensor([0.1,0.3,0.7]).reshape(-1,1)
print(x)

torch.manual_seed(1) # Bunu da görmemiştiniz, o yüzden hazır veriyorum

weight = torch.randn(1, 3)

bias = torch.randn(1, 1)

print(weight)
print(bias)