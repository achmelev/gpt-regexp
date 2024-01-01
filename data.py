from environment import log, get_int_config_value, get_config_value,device

import torch
from exrex import getone
from tokenizer import Tokenizer
from torch import tensor, int64,stack


class DataLoader:

    def __init__(self, useStartIndex = None, validationOff = None):
       
        self.block_size = get_int_config_value("block_size")
        self.batch_size = get_int_config_value("batch_size")
        self.regexp = get_config_value('regexp')
        self.tokenizer = Tokenizer()
        self.tokenizer.load_vocab()

    
    def batch(self):
        samples_list = []
        targets_list = []
        list_size = self.block_size+1
        for i in range(self.batch_size):
            current_tokens = []
            while (len(current_tokens) < list_size):
                text = getone(self.regexp)
                current_tokens+=self.tokenizer.tokenize_text(text)
            if (len(current_tokens) > list_size):
                current_tokens = current_tokens[:list_size]
            samples_list.append(tensor(data=current_tokens[:list_size-1], dtype=int64))
            targets_list.append(tensor(data=current_tokens[1:], dtype=int64))
        samples = stack(samples_list)
        targets = stack(targets_list)

        if device == 'cuda':
            # pin arrays x,y, which allows us to move them to GPU asynchronously (non_blocking=True)
            samples, targets = samples.pin_memory().to(device, non_blocking=True), targets.pin_memory().to(device, non_blocking=True)
        else:
            samples, targets = samples.to(device), targets.to(device)
        return samples, targets

    