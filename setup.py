from setuptools import setup
from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
else:
    use_cython = True
    
cmdclass = { }
#ext_modules = [cythonize('cython/metrics.pyx') ]
ext_modules = []

if use_cython:
    ext_modules += [Extension("correlcalc.metrics", [ "metrics/metrics.pyx" ]),
                                        ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [Extension("correlcalc.metrics", [ "metrics/metrics.c" ]),
                                                ]
setup(
    name='correlcalc',
    version='0.947',
    description='Two-point correlation function (2pCF) calculation',
    url='http://github.com/rohinkumar/correlcalc',
    author='Rohin Kumar Y',
    author_email='yrohinkumar@gmail.com',
    license='MIT',
    packages=['correlcalc','correlcalc.metrics'],
    install_requires=['numpy','scipy','astropy','cython','tqdm','matplotlib','pymangle'],
    cmdclass = cmdclass,
    ext_modules=ext_modules,
    zip_safe=False)