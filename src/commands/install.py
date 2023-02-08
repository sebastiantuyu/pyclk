import os,yaml
from ..utils.context import Context
from ..utils.utils import run_hooks
from ..utils.logger import completed_process, loading_process
from spinners import Spinners
from threading import Thread
import subprocess

def install():
  root_path = Context.root_path
  with open(os.path.join(root_path, 'reqs.yaml'), 'r') as stream:
    Context.project = yaml.safe_load(stream)
  
  packages_list = " ".join(Context.project['packages'])

  if not os.path.isdir(os.path.join(root_path, 'python_modules')):
    print("Creating python_modules folder...")
    os.system(f'cd {root_path}\npython3 -m venv python_modules')

  path_to_python_version = os.path.join(
    root_path,
    "python_modules",
    "lib"
  )
  python_version = os.listdir(path_to_python_version)[0]
  path_to_env_folder = os.path.join(
    root_path,
    "python_modules",
    "lib",
    python_version,
    "site-packages"
  )

  print(f"Installing packages in {path_to_env_folder}...")

  Context.args['c_process'] = True
  p_log = Thread(target=loading_process, args=["Installing full project..."])
  p_install = Thread(target=os.system, args=[f"pip install --quiet {packages_list} --target {path_to_env_folder} --upgrade"])
  p_log.start()
  p_install.start()
  p_install.join()
  Context.args['c_process'] = False
  p_log.join()

  completed_process("\nProject installed successfully")
  ###################
  #                 #
  #    Run hooks    #
  #                 #
  ###################
  run_hooks('install')