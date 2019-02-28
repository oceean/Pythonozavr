from setuptools import setup


readme = ""
with open('readme.md', 'rt', encoding='utf8') as f:
    readme = f.read()
req = ""
with open('requirements.txt', 'rt', encoding='utf8') as f:
    req = f.read()

setup(
    name='MBConnectAgentBase',
    license='MIT',
    author='Gay',
    description='No yet',
    long_description=readme,
    include_package_data=True,
    platforms='any',
    install_requires=req.split("\n"),
)