from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os

VERSION = '0.0.1'

if os.path.isfile('ai2thor/_version.py'):
    exec(open('ai2thor/_version.py').read())


setup(name='ai2thor',
      version=VERSION,
      description='AI2 Thor framework',
      long_description="AI2 Thor is a lightweight AI framework that interacts with the Unity3d Game Engine.",
      classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ],
      keywords='AI2 Thor API',
      url='https://github.com/allenai/ai2thor',
      author='Allen Institute for Artificial Intelligence',
      author_email='ai2thor@allenai.org',
      license='Apache',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[
          'Cython',
          'flask',
          'numpy',
          'pyyaml',
          'requests',
          'progressbar2',
          'botocore',
          'aws-requests-auth',
          'msgpack',
          'Pillow',
          'opencv-python',
          'werkzeug>=0.15.0' # needed for unix socket support
      ],
      tests_require=['pytest', 'pytest-cov', 'jsonschema'],
      include_package_data=False,
      ext_modules = cythonize(
        Extension("ai2thor._x11", ["ai2thor/_x11.pyx"], libraries=["X11", "Xext"], optional=True),
        language_level=3
     )
      
  )
