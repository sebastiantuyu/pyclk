import os,yaml

def install(root_path):
  global project_config
  print("Installing full project...")
  with open(os.path.join(root_path, 'reqs.yaml'), 'r') as stream:
    project_config = yaml.safe_load(stream)
  packages_list = " ".join(project_config['packages'])

  if not os.path.isdir(os.path.join(root_path, 'python_modules')):
    print("Creating python_modules folder...")
    os.system(f'cd {root_path}\npython3 -m venv python_modules')

  activate_script = os.path.join(root_path, "python_modules", "bin", "activate")
  path_to_env_folder = os.path.join(
    root_path,
    "python_modules",
    "lib",
    "python3.8",
    "site-packages"
  )

  os.system(f"pip install {packages_list} --target {path_to_env_folder}")
  # os.system(f"/bin/bash --rcfile {path_to_env_folder}")
  # os.system(f"echo \"hello world\"")