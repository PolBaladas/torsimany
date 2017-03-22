from setuptools import setup
setup(
  name = 'torsimany',
  packages = ['torsimany'],
  version = '1.0',
  description = 'JSON to Markdown converter - Translate any JSON file to stylish, human-readable Markdown.',
  author = 'Pol Baladas',
  author_email = 'polbaladasluna@gmail.com',
  url = 'https://github.com/PolBaladas/torsimany',
  download_url = 'https://github.com/PolBaladas/torsimany/tarball/1.0',
  keywords = ['markdown', 'json', 'convert'], 
  entry_points={
    'console_scripts': [
      'torsimany = torsimany.torsimany:main'
    ]
  },
  classifiers = ['Programming Language :: Python :: 2.7'],
)