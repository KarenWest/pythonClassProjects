from distutils.core import setup, Extension

module1 = Extension('ps8b', sources = ['ps8b.c'])

setup (name = 'ProblemSet8', version = '0.1',
       description = 'Problem Set 8',
       ext_modules = [module1])