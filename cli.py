
import os, yaml, sys
from src.commands.install import install

root_path = os.getcwd()
config_file_path = os.path.join(root_path, 'pyclk.yaml')
config = {
  'services': {}
}

def read_config():
  global config
  try:
    with open(config_file_path, 'r') as stream:
      config = yaml.safe_load(stream)
  except:
    print("Error: Could not load config file.")

def read_args():
  if len(sys.argv) > 2:
    return (sys.argv[1], sys.argv[2])
  else:
    return (sys.argv[1], None)

def run(args):
  if args not in config['services']:
    print("Error: Project not found.")
    print("Hint: Remember to add your project to pyclk.yaml")
    return

  global inner_config
  app_relative_path = os.path.join(root_path, config['services'][args]['path'])
  try:
    with open(os.path.join(app_relative_path, 'reqs.yaml'), 'r') as stream:
      inner_config = yaml.safe_load(stream)
    os.system(
      f"cd {app_relative_path}\n{inner_config['scripts']['run']}"
    )
  except:
    print("Error: Reqs file not found in project.")

def run_command(cmd, args):
  print(cmd)
  if cmd == 'run':
    run(args)
  elif cmd == 'install':
    install(root_path)
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

  run_command(command, project)
