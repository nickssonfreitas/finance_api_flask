from setuptools import setup, find_packages

setup(
    name='finance_api_flask',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'pytest',
        # adicione outras dependências necessárias aqui
    ],
)
