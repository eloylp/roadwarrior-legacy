import os

from setuptools import setup
import re
import roadwarrior

here = os.path.abspath(os.path.dirname(__file__))

try:

    with open(here + '/README.md') as r:
        readme_html = r.read()
        readme_plain = re.sub(r"<([0-9a-zA-Z/]*)>", "", readme_html)

    with open(here + '/requirements.txt') as req:
        reqs = req.read().splitlines()
except:

    reqs = list()
    readme_plain = ''

setup(
    name='scirocco-pyclient',
    version=roadwarrior.__version__,
    download_url='https://github.com/eloylp/scirocco-pyclient/tarball/' + roadwarrior.__version__,
    url='https://github.com/eloylp/scirocco-pyclient',
    license='GNU AFFERO 3',
    author='eloylp',
    install_requires=reqs,
    author_email='eloy@sandboxwebs.com',
    description='',
    test_suite='test',
    long_description=readme_plain,
    packages=['roadwarrior'],
    classifiers=[
        
    ],
    include_package_data=True,
    platforms='any'
)
