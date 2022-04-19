from setuptools import setup, find_packages

setup(
    name='pyqt-responsive-label',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QLabel which can resize the font responsively accordance with window\'s size change',
    url='https://github.com/yjg30737/pyqt-responsive-label.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)