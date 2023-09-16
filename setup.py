from skbuild import setup

setup(
    name='hana_learn',
    version='0.0.1',
    description='Learning environment for the game of hanabi.',
    author='ffrujeri/hana-learn',
    packages=['hana_learn'],
    install_requires=['cffi']
)
