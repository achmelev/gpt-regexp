from environment import initEnv, get_int_config_value,log, get_config_value
from sys import argv
from exrex import getone

if (len(argv) < 3):
    raise Exception('Called with less as 2 arguments')

initEnv(argv[1])

from environment import log


command = argv[2]
args = None
if (len(argv) > 3):
    args = argv[3:]


        
if (command == 'exrex'):
    regexp = get_config_value('regexp')
    log.info("Generated String: "+getone(regexp))
else:
    raise Exception('Unknown command: '+command)



