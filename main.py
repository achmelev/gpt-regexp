from environment import initEnv, get_int_config_value,log, get_config_value
from sys import argv
from exrex import getone


if (len(argv) < 3):
    raise Exception('Called with less as 2 arguments')

initEnv(argv[1])

from environment import log
from generator import TextGenerator
from train import Trainer


command = argv[2]
args = None
if (len(argv) > 3):
    args = argv[3:]

def do_generate(args):
    if (args == None):
        prompt = ""
    else:
        prompt = args[0]
    generator = TextGenerator(prompt = prompt)
    generator.generate_console()

def do_train(args):
    if (args == None):
        log.error("Wrong number of arguments for command train")
    else:
        minutes_to_train = int(args[0])
        trainer = Trainer(minutes_to_train)
        trainer.run()



if (command == 'exrex'):
    regexp = get_config_value('regexp')
    log.info("Generated String: "+getone(regexp))
elif (command == 'generate'):
    do_generate(args)
elif (command == 'train'):
    do_train(args)
else:
    raise Exception('Unknown command: '+command)



