from environment import initEnv, get_int_config_value,log
from sys import argv

if (len(argv) < 3):
    raise Exception('Called with less as 2 arguments')

initEnv(argv[1])

from environment import log


command = argv[2]
args = None
if (len(argv) > 3):
    args = argv[3:]


        
if (command == 'helloworld'):
    log.info("Hello World!")
else:
    raise Exception('Unknown command: '+command)



