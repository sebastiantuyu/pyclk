from setuptools import setup
import yaml

with open("reqs.yaml", "r") as f:
  version = yaml.safe_load(f)["version"]

if __name__ == "__main__":
  print("Running setup.py")
  setup(
    name='pyclk',
    version=version,
    scripts=[
      'cli.py'
    ],
    install_requires=[
      'pyyaml',
      'spinners'
    ],
    entry_points={
      'console_scripts': [
        'pyclk = cli:main'
      ]
    }
  )