from setuptools import find_packages, setup

package_name = 'tarefarobo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pato',
    maintainer_email='felipiniobrsp@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = tarefarobo.publisher_python:main',
            'subscriber = tarefarobo.subscriber_python:main',
            'number_publisher = tarefarobo.number_publisher:main',
            'number_count = tarefarobo.number_count:main',
        ],
    },
)
