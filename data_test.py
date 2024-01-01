import unittest
from environment import initEnv, get_int_config_value
from shutil import rmtree

class DataLoaderTest (unittest.TestCase):

    def setUp(self) -> None:
        initEnv('unittest')
        
    
    def tearDown(self) -> None:
        from environment import workDir
        rmtree(workDir)
    
    def test_batch(self):
        from environment import log
        from data import DataLoader
        loader = DataLoader()
        batch = loader.batch()

        block_size = get_int_config_value("block_size")
        batch_size = get_int_config_value("batch_size")

        samples = batch[0]
        targets = batch[1]
        self.assertEqual(samples.size(dim=0), batch_size)
        self.assertEqual(samples.size(dim=1), block_size)
        self.assertEqual(targets.size(dim=0), batch_size)
        self.assertEqual(targets.size(dim=1), block_size)

    
if __name__ == '__main__':
    unittest.main()

