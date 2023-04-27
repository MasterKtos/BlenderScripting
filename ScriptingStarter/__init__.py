# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ScriptingStarter",
    "author" : "MasterKtos",
    "description" : "",
    "blender" : (3, 4, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from .SimpleOperator import TestOperator

# Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(TestOperator.bl_idname, text=TestOperator.bl_label)

def register():
    # Add class to Blender
    bpy.utils.register_class(TestOperator)
    # Remove class from spacebar menu (if previously added)
    for f in bpy.types.VIEW3D_MT_view._dyn_ui_initialize():
        if f.__name__ == menu_func.__name__:
            bpy.types.VIEW3D_MT_view.remove(f)
            break
    # Add class to spacebar menu
    bpy.types.VIEW3D_MT_view.append(menu_func)

def unregister():
    # Remove class from Blender
    bpy.utils.unregister_class(TestOperator)

if __name__=="__main__":
    register()