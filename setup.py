from setuptools import setup


setup(
        name='novaclient-auth-secretkey',
        version='0.1',
        author='fr33jc',
        author_email='fr33jc@gmail.com',
        packages=['novaclient_secretkey'],
        license='MIT',
        description=('Authentication plugin for novaclient enabling '
            'API key and secret key'),
        install_requires=['python-novaclient'],
        entry_points={
            'openstack.client.authenticate': [
                'secretkey = novaclient_secretkey.auth_plugin:secretkey',
                ],
            },
        )
