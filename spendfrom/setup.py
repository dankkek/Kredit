from distutils.core import setup
setup(name='DKKspendfrom',
      version='1.0',
      description='Command-line utility for Kredit "coin control"',
      author='Gavin Andresen',
      author_email='gavin@Kreditfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
