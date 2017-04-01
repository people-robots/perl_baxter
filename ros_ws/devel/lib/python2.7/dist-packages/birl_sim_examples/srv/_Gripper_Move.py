# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from birl_sim_examples/Gripper_MoveRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Gripper_MoveRequest(genpy.Message):
  _md5sum = "871caa371d500d7fa688824bad2884cb"
  _type = "birl_sim_examples/Gripper_MoveRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
std_msgs/Bool gripper_desired_flag


================================================================================
MSG: std_msgs/Bool
bool data"""
  __slots__ = ['gripper_desired_flag']
  _slot_types = ['std_msgs/Bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       gripper_desired_flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Gripper_MoveRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.gripper_desired_flag is None:
        self.gripper_desired_flag = std_msgs.msg.Bool()
    else:
      self.gripper_desired_flag = std_msgs.msg.Bool()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.gripper_desired_flag.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.gripper_desired_flag is None:
        self.gripper_desired_flag = std_msgs.msg.Bool()
      end = 0
      start = end
      end += 1
      (self.gripper_desired_flag.data,) = _struct_B.unpack(str[start:end])
      self.gripper_desired_flag.data = bool(self.gripper_desired_flag.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.gripper_desired_flag.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.gripper_desired_flag is None:
        self.gripper_desired_flag = std_msgs.msg.Bool()
      end = 0
      start = end
      end += 1
      (self.gripper_desired_flag.data,) = _struct_B.unpack(str[start:end])
      self.gripper_desired_flag.data = bool(self.gripper_desired_flag.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from birl_sim_examples/Gripper_MoveResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class Gripper_MoveResponse(genpy.Message):
  _md5sum = "8d9e11dac10874c976cb4e10995e82c8"
  _type = "birl_sim_examples/Gripper_MoveResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


std_msgs/Bool gripper_status_flag


================================================================================
MSG: std_msgs/Bool
bool data"""
  __slots__ = ['gripper_status_flag']
  _slot_types = ['std_msgs/Bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       gripper_status_flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Gripper_MoveResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.gripper_status_flag is None:
        self.gripper_status_flag = std_msgs.msg.Bool()
    else:
      self.gripper_status_flag = std_msgs.msg.Bool()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.gripper_status_flag.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.gripper_status_flag is None:
        self.gripper_status_flag = std_msgs.msg.Bool()
      end = 0
      start = end
      end += 1
      (self.gripper_status_flag.data,) = _struct_B.unpack(str[start:end])
      self.gripper_status_flag.data = bool(self.gripper_status_flag.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.gripper_status_flag.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.gripper_status_flag is None:
        self.gripper_status_flag = std_msgs.msg.Bool()
      end = 0
      start = end
      end += 1
      (self.gripper_status_flag.data,) = _struct_B.unpack(str[start:end])
      self.gripper_status_flag.data = bool(self.gripper_status_flag.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class Gripper_Move(object):
  _type          = 'birl_sim_examples/Gripper_Move'
  _md5sum = '16b119fdb1caa4ce59870b158835a73f'
  _request_class  = Gripper_MoveRequest
  _response_class = Gripper_MoveResponse