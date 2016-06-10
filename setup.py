from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cwru',
      version='0.2',
      description='Case Western Reserve University Bearing Data',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Information Analysis',
      ],
      keywords='cwru bearing fault diagnosis dataset',
      url='https://github.com/Litchiware/cwru',
      author='Liangmin Li',
      author_email='1508490934@qq.com',
      license='MIT',
      packages=['cwru'],
      install_requires=[
          'numpy',
          'scipy',
      ],
      include_package_data=True,
      test_suite='tests',
      zip_safe=False)
