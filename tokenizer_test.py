import unittest

from environment import initEnv
from shutil import rmtree
from os.path import join, isfile


class TokenizerTest (unittest.TestCase):

    def setUp(self) -> None:
        initEnv('unittest')
        
    
    def tearDown(self) -> None:
        from environment import workDir
        rmtree(workDir)
    
    
    def test_tokenize(self):
        from environment import log
        from tokenizer import Tokenizer
        tokenizer = Tokenizer()
        tokenizer.load_vocab()

        input_text = "12+15 21-95 56+21*3"
        target_text = "12+15 21-95 56+21*3"
        
        tokens = tokenizer.tokenize_text(input_text)
        tokenizer.verify_tokens(tokens)
        text_again = tokenizer.tokens_to_text(tokens)

        self.assertEqual(text_again, target_text)
    
if __name__ == '__main__':
    unittest.main()