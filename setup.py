# ***********************************************************************************
# * Copyright 2019 Jonathon Brunson. All rights reserved.                           * 
# *                                                                                 *
# * Redistribution and use in source and binary forms, with or without              *
# * modification, are permitted provided that the following conditions are met:     *
# *                                                                                 *
# *  1. Redistributions of source code must retain the above copyright notice,      *
# *  this list of conditions and the following disclaimer.                          *
# *                                                                                 *
# *  2. Redistributions in binary form must reproduce the above copyright notice,   *
# *  this list of conditions and the following disclaimer in the documentation      *
# *  and/or other materials provided with the distribution.                         *
# *                                                                                 *
# * THIS SOFTWARE IS PROVIDED BY JONATHON BRUNSON ``AS IS'' AND ANY EXPRESS OR      *
# * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF    *
# * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO      *
# * EVENT SHALL <COPYRIGHT HOLDER> OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,        *
# * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,  *
# * BUT NOT LIMITED TO, PROCUREMEN OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,    *
# * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY           *
# * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING  *
# * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS              *
# * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                    *
# ***********************************************************************************

# CHECK THIS PATCH
#try:
#    from setuptools import setup
#except ImportError:
from distutils.core import setup
from src.version import PYGTV_VERSION

import numpy as np

def readme(fname):
    with open(fname, 'r') as f:
        return f.read()

setup(
    name = 'shapefile-vtk',
    version = PYGTV_VERSION,
    description = 'Exports GIS data as binary VTK files',
    long_description = readme('README.md'),
    author = 'Jonathon Brunson',
    author_email = 'jonathonbrunson21@gmail.com',
    url = 'https://github.com/jonathonb21/shapefile-vtk.git',
    packages = ['gtv'],
    package_dir = {'gtv' : 'src'},
    package_data = {'gtv' :  ['LICENSE', 'examples/*.py', 'files/*.py', 'shapes/*.py']},
    scripts=['src/shapeToVTK.py'],
    project_urls={
        "Bug Tracker": "http://github.com/jonathonb21/shapefile-vtk",
        "Documentation": "http://github.com/jonathonb21/shapefile-vtk",
        "Source Code": "http://github.com/jonathonb21/shapefile-vtk",
    }
)

