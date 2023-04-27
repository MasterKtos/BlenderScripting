from math import radians
import bpy
from bpy.props import (FloatProperty)

class TestOperator(bpy.types.Operator):
    """Hi!"""
    bl_idname = "object.simple_operator"
    bl_label = "Test Operator"
    bl_description = "Test description"
    bl_options = {'REGISTER', 'UNDO'}

    magic_property : FloatProperty(
        name = "Magic property",
        description = "Driver for the whole operator",
        default = 1.0,
        min = -10,
        max = 10
    )


    # Called when user selects "Simple Operator" from the spacebar menu
    def execute(self, context):
        self.report({'INFO'}, "Hello World!")
        selected = bpy.context.active_object;
        selected.location[2] += self.magic_property
        selected.rotation_euler[2] += radians(30 * self.magic_property)

        return {'FINISHED'}
    
