from skbuild import setup

setup(
    name='hana_learn',
    version='0.0.1',
    description='Learning environment for the game of hanabi.',
    author='ffrujeri/hana_learn',
    packages=['hana_learn', 'hana_learn.agents'],
    install_requires=['cffi']
)
