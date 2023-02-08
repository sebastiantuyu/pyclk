
import os, yaml, sys
from src.commands.install import install
from src.commands.run import run
from src.commands.build import build
from src.commands.activate import activate
from src.utils.context import Context
from src.utils.logger import loading_process


Context.set_root_path(os.getcwd())
Context.config_file_path = os.path.join(Context.root_path, 'pyclk.yaml')

def read_config():
  global config
  try:
    with open(Context.config_file_path, 'r') as stream:
      Context.config = yaml.safe_load(stream)
  except:
    print("Error: Could not load config file.")

def read_args():
  if len(sys.argv) > 2:
    return (sys.argv[1], sys.argv[2])
  elif len(sys.argv) == 1:
    return (None, None)
  
  return (sys.argv[1], None)

def run_command(cmd, args):
  if cmd == 'run':
    run()
  elif cmd == 'activate':
    activate()
  elif cmd == 'install':
    install()
  elif cmd == 'build':
    build()
  elif cmd == 'version':
    print('0.0.1')
  else:
    print("Error: Command not found")

def main():
  """
    Execute validation checks,
    and parse config files
  """
  read_config()
  (command, project) = read_args()
  if command is None:
    print("PyCLK v0.0.1")
    sys.exit(0)
  Context.command['args'] = project
  Context.command['command'] = command

  run_command(command, project)
