try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A text-based adventure written in Python',
    'author': 'Calvin Xu',
    'url': 'https://github.com/Calvin-Xu/Precarious_Game',
    'download_url': 'https://github.com/Calvin-Xu/Precarious_Game',
    'author_email': 'calvinxu806@vip.163.com',
    'version': '1.0.0',
    'install_requires': ['pytest'],
    'packages': ['Game'],
    'scripts': [],
    'name': 'precarious'
}

setup(**config)
