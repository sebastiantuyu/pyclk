class _ServiceContext:
  def __init__(self):
    self.config = {}
    self.root_path = ""
    self.config_file_path = ""
    self.command = {
      'args': [],
      'command': '',
    }
    self.project = {}
    self.args = {}

  def set_config(self, config):
    self.config = config
  
  def set_root_path(self, root_path):
    self.root_path = root_path

  def set_config_file_path(self, config_file_path):
    self.config_file_path = config_file_path
  
  def get_config(self):
    return self.config
  
  def get_root_path(self):
    return self.root_path
  
  def get_config_file_path(self):
    return self.config_file_path

Context = _ServiceContext()