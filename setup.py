from setuptools import setup

if __name__ == "__main__":
  print("Running setup.py")
  setup(
    name='pyclk',
    version='0.0.1',
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