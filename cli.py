
import yaml
import os

root_path = os.getcwd()
config_file_path = os.path.join(root_path, 'pyclk.yaml')
config = {}

def read_config():
  global config
  try:
    with open(config_file_path, 'r') as stream:
      config = yaml.safe_load(stream)
  except:
    print("Error: Could not load config file.")

def main():
  read_config()

  print("Running PyClk...")
