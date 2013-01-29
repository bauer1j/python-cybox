import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_pipe_object_1_2 as win_pipe_object_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.objects.pipe_object import pipe_object
from cybox.objects.win_handle_object import win_handle_object

class win_pipe_object:
    def __init__(self):
        pass
        
    @classmethod
    def create_from_dict(cls, win_pipe_attributes):
        win_pipe_obj = pipe_object.create_from_dict(win_pipe_attributes, win_pipe_object_binding.WindowsPipeObjectType())
        win_pipe_obj.set_anyAttributes_({'xsi:type' : 'WinPipeObj:WindowsPipeObjectType'})
        
        for key, value in win_pipe_attributes.items():
            if key == 'default_time_out' and common_methods.test_value(value):
                win_pipe_obj.set_Default_Time_Out(baseobjectattribute.create_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'handle':
                win_pipe_obj.set_Handle(win_handle_object.create_from_dict(value))
            elif key == 'in_buffer_size' and common_methods.test_value(value):
                win_pipe_obj.set_In_Buffer_Size(baseobjectattribute.create_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'max_instances' and common_methods.test_value(value):
                win_pipe_obj.set_Max_Instances(baseobjectattribute.create_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'open_mode' and common_methods.test_value(value):
                win_pipe_obj.set_Open_Mode(baseobjectattribute.create_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'out_buffer_size' and common_methods.test_value(value):
                win_pipe_obj.set_Out_Buffer_Size(baseobjectattribute.create_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'pipe_mode' and common_methods.test_value(value):
                win_pipe_obj.set_Pipe_Mode(baseobjectattribute.create_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'security_attributes' and common_methods.test_value(value):
                win_pipe_obj.set_Security_Attributes(baseobjectattribute.create_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))

        return win_pipe_obj

    @classmethod
    def parse_into_dict(cls, defined_object):
        defined_object_dict = pipe_object.parse_into_dict(defined_object)
        if defined_object.get_Default_Time_Out() is not None: defined_object_dict['default_time_out'] = baseobjectattribute.parse_into_dict(defined_object.get_Default_Time_Out())
        if defined_object.get_Handle() is not None: defined_object_dict['handle'] = win_handle_object.parse_into_dict(defined_object.get_Handle())
        if defined_object.get_In_Buffer_Size() is not None: defined_object_dict['in_buffer_size'] = baseobjectattribute.parse_into_dict(defined_object.get_In_Buffer_Size())
        if defined_object.get_Max_Instances() is not None: defined_object_dict['max_instances'] = baseobjectattribute.parse_into_dict(defined_object.get_Max_Instances())
        if defined_object.get_Open_Mode() is not None: defined_object_dict['open_mode'] = baseobjectattribute.parse_into_dict(defined_object.get_Open_Mode())
        if defined_object.get_Out_Buffer_Size() is not None: defined_object_dict['out_buffer_size'] = baseobjectattribute.parse_into_dict(defined_object.get_Out_Buffer_Size())
        if defined_object.get_Pipe_Mode() is not None: defined_object_dict['pipe_mode'] = baseobjectattribute.parse_into_dict(defined_object.get_Pipe_Mode())
        if defined_object.get_Security_Attributes() is not None: defined_object_dict['security_attributes'] = baseobjectattribute.parse_into_dict(defined_object.get_Security_Attributes())
        return defined_object




