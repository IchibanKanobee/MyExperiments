import torch
import torch.nn.functional as F
#import matplotlib.pyplot as plt # for making figures

words = open('names.txt', 'r').read().splitlines()
print (words[:8])

# build the vocabulary of characters and mappings to/from integers
chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}
print(itos)

block_size = 3  # context length: how many characters do we take to predict the next one?
X, Y = [], []
for w in words[:5]:

    # print(w)
    context = [0] * block_size
    for ch in w + '.':
        ix = stoi[ch]
        X.append(context)
        Y.append(ix)
        tmp = (''.join(itos[i] for i in context))
        print(''.join(itos[i] for i in context), '--->', itos[ix])
        context = context[1:] + [ix]  # crop and append

X = torch.tensor(X)
Y = torch.tensor(Y)