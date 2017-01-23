from setuptools import setup
setup(
  name = 'torsimany',
  packages = ['torsimany'],
  version = '0.17',
  description = 'JSON to Markdown converter - Translate any JSON file to stylish, human-readable Markdown.',
  author = 'Pol Baladas',
  author_email = 'polbaladasluna@gmail.com',
  url = 'https://github.com/PolBaladas/torsimany',
  download_url = 'https://github.com/PolBaladas/torsimany/tarball/0.17',
  keywords = ['markdown', 'json', 'convert'], 
  entry_points={
    'console_scripts': [
      'torsimany = torsimany.torsimany:main'
    ]
  },
  classifiers = ['Programming Language :: Python :: 2.7'],
)