from os import path

from setuptools import find_packages, setup

# Get the version from bbb_dl/version.py without importing the package
exec(compile(open('bbb_dl/version.py', encoding="utf-8").read(), 'bbb_dl/version.py', 'exec'))


def readme():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name='bbb-dl',
    version=__version__,
    description='Big Blue Button Downloader that downloads a BBB lesson as MP4 video',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/C0D3D3V/bbb-dl',
    author='C0D3D3V',
    license='GPL-2.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bbb-dl = bbb_dl.main:main',
            'bbb-dl-batch = bbb_dl.batch:main',
            'bbb-dl-browser = bbb_dl.browser:main',
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        'aiofiles>=22.1.0',
        'aiohttp>=3.8.3',
        'colorama>=0.4.6',
        'playwright>=1.29.0',
        'PySide6>=6.5.0',
        'python-ffmpeg>=1.0.16',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
