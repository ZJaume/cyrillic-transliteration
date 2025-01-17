from distutils.core import setup
setup(
  name='cyrtranslit',
  packages=['cyrtranslit'],
  version='1.0',
  description='Bi-directional Cyrillic transliteration. Transliterate Cyrillic script to Latin script and vice versa.',
  author='Georges Labrèche, Open Data Kosovo',
  author_email='georges@tanagraspace.com',
  url='https://github.com/opendatakosovo/cyrillic-transliteration',
  download_url='https://github.com/opendatakosovo/cyrillic-transliteration/archive/v1.0.tar.gz',
  license='MIT',
  long_description='Transliteration is the conversion of a text from one script to another. Current version supports transliteration for Bulgarian, Montenegrin, Macedonian, Russian, Serbian, Tajik, and Ukrainian.',
  keywords=['cyrillic', 'latin', 'transliteration', 'transliterate', 'cyrtranslit', 'bulgarian', 'montenegrin', 'macedonian', 'russian', 'serbian', 'tajik', 'ukrainian'],
  classifiers=['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8'],
  entry_points={
      "console_scripts": [
          "cyrtranslit=cyrtranslit.cyrtranslit:main",
      ]
  },
)
