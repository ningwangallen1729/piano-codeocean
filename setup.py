"""
PIANO: Probabilistic Inference Autoencoder Networks for multi-Omics
Copyright (C) 2025 Ning Wang

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

setup(
    name='PIANO',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-misc',
        'anndata',
        'scanpy',
        'torch',
    ],
    extras_require={
        'rapids': [
            'jax[cuda12]',
            'rapids-singlecell[rapids12]==0.12.7'
        ],
        'scvi-tools': [
            'scvi-tools',
            'scib-metrics==0.5.3'
        ],
        'torch': [
            'torchvision',
            'torchaudio',
        ],
        'misc': [
            'igraph'
            'leidenalg'
            'matplotlib'
            'seaborn'
            'joblib'
            'jupyterlab'
            'pot'
        ],
        'all': [
            'igraph',
            'leidenalg',
            'torchvision',
            'torchaudio',
            'scvi-tools',
            'scib-metrics==0.5.3',
            'jax[cuda12]',
            'rapids-singlecell[rapids12]==0.12.7',
            'matplotlib',
            'seaborn',
            'joblib',
            'jupyterlab',
            'pot',
        ],
    },
    author='Ning Wang',
    description='PIANO - Probabilistic Inference Autoencoder Networks for multi-Omics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ningwang1729/piano',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    license='GPLv3',
)
