from environment import log
from environment import get_config_value, get_int_config_value,get_bool_config_value,workDir




class Tokenizer:
   def  __init__(self, validationOf = None):
      #get chars
      self.chars = get_config_value('chars')

   
   def prepare_vocab_map(self):
      self.vocab_map = {value: index for index, value in enumerate(self.vocab)}


   def load_vocab(self):
      log.info("Loading vocab")
      self.vocab = []
      for c in self.chars:
         self.vocab.append(c)
      self.vocab.append('#')
      self.prepare_vocab_map()
      self.vocab_prepared = True

   def tokenize_text(self, text):
      assert self.vocab_prepared, 'no vocab'
      words = text.split()
      tokens = []
      for word in words:
         tokens.append(self.vocab_map['#'])
         for c in word:
            tokens.append(self.vocab_map[c])
      return tokens
   
   def tokens_to_text(self, tokens):
      assert  not any(t not in range(len(self.vocab)) for t in tokens)

      result = ""
      begin = True
      for t in tokens:
         text_token = self.vocab[t]
         if (text_token == '#'):
            if len(result) > 0:
               result = result + ' '
         else:
            result = result + text_token
      return result
         
   def verify_tokens(self, tokens):
      assert self.vocab_prepared, 'no vocab'
      log.info('Verifying tokens')
      assert  not any(t >= len(self.vocab) for t in tokens)


  




