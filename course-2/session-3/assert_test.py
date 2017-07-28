#!/home/rob/.pyenv/shims/python3

def example(param):
  """param must be greater than 0"""
  assert param > 0
  #if __debug__:
  #  if not param > 0:
  #    raise AssertionError
  # do stuff here...

if __name__ == '__main__':
  example(0)