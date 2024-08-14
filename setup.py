import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'duo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('urdf/*.urdf')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='deadcat',
    maintainer_email='artem.nkfv@gmail.com',
    description='Dual motor robot libraries package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'circle_publisher = duo.circle_publisher:main',
            'encoder_publisher = duo.encoder_publisher:main'
        ],
    },
)
