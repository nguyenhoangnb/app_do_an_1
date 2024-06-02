from setuptools import setup, find_packages

# with open('README.md', 'r', encoding='utf-8') as readme_file:
#     long_description = readme_file.read()

setup(
    name='system_info',
    version='1.0.0',
    description='Check system current CPU and RAM utilization percentage.',
    long_description="long_description",
    author='Nguyen Hoang',
    author_email='nguyenhoang.uet12@gmail.com',
    license='MIT',
    install_requires=['psutil'],
    packages=find_packages(),
    # packages=['sysinfo'],
    package_dir={'': '/'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux'
    ],
    entry_points=dict(
        console_scripts=['system_info=system_info.cpu_memory_utilization:main']
    ),
    data_files=[
        ('', ['system_utilization.desktop'])
    ],
    keywords='CPU RAM Memory Utilization'
)