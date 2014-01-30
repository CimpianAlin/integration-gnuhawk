#
# This file is protected by Copyright. Please refer to the COPYRIGHT file 
# distributed with this source distribution.
# 
# This file is part of GNUHAWK.
# 
# GNUHAWK is free software: you can redistribute it and/or modify is under the 
# terms of the GNU General Public License as published by the Free Software 
# Foundation, either version 3 of the License, or (at your option) any later 
# version.
# 
# GNUHAWK is distributed in the hope that it will be useful, but WITHOUT ANY 
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with 
# this program.  If not, see http://www.gnu.org/licenses/.
#
from redhawk.codegen.jinja.common import ShellTemplate, SpecfileTemplate
from redhawk.codegen.jinja.project.component.mapping import ProjectMapper
from redhawk.codegen.jinja.project.component.generator import ComponentProjectGenerator
from redhawk.codegen.jinja.loader import CodegenLoader

if not '__package__' in locals():
    # Python 2.4 compatibility
    __package__ = __name__.rsplit('.', 1)[0]

loader = CodegenLoader(__package__,
                       {'base'       : 'redhawk.codegen.jinja.project.component'})

class GnuhawkComponentProjectGenerator(ComponentProjectGenerator):
    def projectMapper(self):
        return ProjectMapper()

    def loader(self, project):
        return loader

    def templates(self, project):   
        return [
            ShellTemplate('base/build.sh'),
            SpecfileTemplate('component.spec', project['name']+'.spec')
            ]
