# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from force_controller/forceControlRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class forceControlRequest(genpy.Message):
  _md5sum = "cda3fb843d195f1bf40697fef6470230"
  _type = "force_controller/forceControlRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
int32 num_ctrls


string domType


geometry_msgs/Vector3[] domDes


geometry_msgs/Vector3[] domGains


string subType


geometry_msgs/Vector3[] subDes


geometry_msgs/Vector3[] subGains


================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['num_ctrls','domType','domDes','domGains','subType','subDes','subGains']
  _slot_types = ['int32','string','geometry_msgs/Vector3[]','geometry_msgs/Vector3[]','string','geometry_msgs/Vector3[]','geometry_msgs/Vector3[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       num_ctrls,domType,domDes,domGains,subType,subDes,subGains

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(forceControlRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.num_ctrls is None:
        self.num_ctrls = 0
      if self.domType is None:
        self.domType = ''
      if self.domDes is None:
        self.domDes = []
      if self.domGains is None:
        self.domGains = []
      if self.subType is None:
        self.subType = ''
      if self.subDes is None:
        self.subDes = []
      if self.subGains is None:
        self.subGains = []
    else:
      self.num_ctrls = 0
      self.domType = ''
      self.domDes = []
      self.domGains = []
      self.subType = ''
      self.subDes = []
      self.subGains = []

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
      buff.write(_struct_i.pack(self.num_ctrls))
      _x = self.domType
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.domDes)
      buff.write(_struct_I.pack(length))
      for val1 in self.domDes:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.domGains)
      buff.write(_struct_I.pack(length))
      for val1 in self.domGains:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self.subType
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.subDes)
      buff.write(_struct_I.pack(length))
      for val1 in self.subDes:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.subGains)
      buff.write(_struct_I.pack(length))
      for val1 in self.subGains:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.domDes is None:
        self.domDes = None
      if self.domGains is None:
        self.domGains = None
      if self.subDes is None:
        self.subDes = None
      if self.subGains is None:
        self.subGains = None
      end = 0
      start = end
      end += 4
      (self.num_ctrls,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.domType = str[start:end].decode('utf-8')
      else:
        self.domType = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.domDes = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.domDes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.domGains = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.domGains.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.subType = str[start:end].decode('utf-8')
      else:
        self.subType = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subDes = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.subDes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subGains = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.subGains.append(val1)
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
      buff.write(_struct_i.pack(self.num_ctrls))
      _x = self.domType
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.domDes)
      buff.write(_struct_I.pack(length))
      for val1 in self.domDes:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.domGains)
      buff.write(_struct_I.pack(length))
      for val1 in self.domGains:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self.subType
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.subDes)
      buff.write(_struct_I.pack(length))
      for val1 in self.subDes:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.subGains)
      buff.write(_struct_I.pack(length))
      for val1 in self.subGains:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.domDes is None:
        self.domDes = None
      if self.domGains is None:
        self.domGains = None
      if self.subDes is None:
        self.subDes = None
      if self.subGains is None:
        self.subGains = None
      end = 0
      start = end
      end += 4
      (self.num_ctrls,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.domType = str[start:end].decode('utf-8')
      else:
        self.domType = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.domDes = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.domDes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.domGains = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.domGains.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.subType = str[start:end].decode('utf-8')
      else:
        self.subType = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subDes = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.subDes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.subGains = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.subGains.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_3d = struct.Struct("<3d")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from force_controller/forceControlResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class forceControlResponse(genpy.Message):
  _md5sum = "d5fc6b37f5643970fe87c91f31f11e4a"
  _type = "force_controller/forceControlResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
int32 output

"""
  __slots__ = ['output']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       output

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(forceControlResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.output is None:
        self.output = 0
    else:
      self.output = 0

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
      buff.write(_struct_i.pack(self.output))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.output,) = _struct_i.unpack(str[start:end])
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
      buff.write(_struct_i.pack(self.output))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.output,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
class forceControl(object):
  _type          = 'force_controller/forceControl'
  _md5sum = '33800c3c3d1a1e0744d81c70e60d4c00'
  _request_class  = forceControlRequest
  _response_class = forceControlResponse