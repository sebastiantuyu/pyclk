
import os, yaml, sys
from inspect import getmembers
import src
# from src.commands.install import install
# from src.commands.run import run
# from src.commands.build import build
# from src.commands.activate import activate
from src.utils.context import Context
from src.utils.logger import loading_process
from src.utils.chalk import chalk
from src.utils.utils import run_hooks


Context.root_path = os.getcwd()
Context.config_file_path = os.path.join(Context.root_path, 'pyclk.yaml')
Context.commands = getattr(sys.modules['src'], 'commands')

def read_config():
  global config
  try:
    with open(Context.config_file_path, 'r') as stream:
      Context.config = yaml.safe_load(stream)
  except:
    print("Error: Could not load config file.")

def read_args():
  if len(sys.argv) >= 1:
    return (None, None)
  return (sys.argv[1], sys.argv[2])

def run_command(cmd, args):
  try:
    Context.get_command(cmd)()

    ###################
    #                 #
    #    Run hooks    #
    #                 #
    ###################
    run_hooks(cmd)
  except:
    chalk.red("Error: Command not found")

def main():
  """
    Execute validation checks,
    and parse config files
  """
  read_config()
  (command, project) = read_args()
  if command is None:
    chalk.green("PyCLK v0.0.1")
    sys.exit(0)

  Context.command['args'] = project
  Context.command['command'] = command

  run_command(command, project)
