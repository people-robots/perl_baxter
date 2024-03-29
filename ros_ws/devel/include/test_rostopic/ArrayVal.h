// Generated by gencpp from file test_rostopic/ArrayVal.msg
// DO NOT EDIT!


#ifndef TEST_ROSTOPIC_MESSAGE_ARRAYVAL_H
#define TEST_ROSTOPIC_MESSAGE_ARRAYVAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <test_rostopic/Val.h>

namespace test_rostopic
{
template <class ContainerAllocator>
struct ArrayVal_
{
  typedef ArrayVal_<ContainerAllocator> Type;

  ArrayVal_()
    : vals()  {
    }
  ArrayVal_(const ContainerAllocator& _alloc)
    : vals(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::test_rostopic::Val_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::test_rostopic::Val_<ContainerAllocator> >::other >  _vals_type;
  _vals_type vals;




  typedef boost::shared_ptr< ::test_rostopic::ArrayVal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_rostopic::ArrayVal_<ContainerAllocator> const> ConstPtr;

}; // struct ArrayVal_

typedef ::test_rostopic::ArrayVal_<std::allocator<void> > ArrayVal;

typedef boost::shared_ptr< ::test_rostopic::ArrayVal > ArrayValPtr;
typedef boost::shared_ptr< ::test_rostopic::ArrayVal const> ArrayValConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_rostopic::ArrayVal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_rostopic::ArrayVal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_rostopic

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'test_rostopic': ['/home/ai05/ros_ws/src/ros_comm/test/test_rostopic/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_rostopic::ArrayVal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_rostopic::ArrayVal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rostopic::ArrayVal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_rostopic::ArrayVal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rostopic::ArrayVal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_rostopic::ArrayVal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_rostopic::ArrayVal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "94e095e6a59bceb3466e4b23c166732e";
  }

  static const char* value(const ::test_rostopic::ArrayVal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x94e095e6a59bceb3ULL;
  static const uint64_t static_value2 = 0x466e4b23c166732eULL;
};

template<class ContainerAllocator>
struct DataType< ::test_rostopic::ArrayVal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_rostopic/ArrayVal";
  }

  static const char* value(const ::test_rostopic::ArrayVal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_rostopic::ArrayVal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Val[] vals\n\
================================================================================\n\
MSG: test_rostopic/Val\n\
string val\n\
";
  }

  static const char* value(const ::test_rostopic::ArrayVal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_rostopic::ArrayVal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.vals);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ArrayVal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_rostopic::ArrayVal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test_rostopic::ArrayVal_<ContainerAllocator>& v)
  {
    s << indent << "vals[]" << std::endl;
    for (size_t i = 0; i < v.vals.size(); ++i)
    {
      s << indent << "  vals[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::test_rostopic::Val_<ContainerAllocator> >::stream(s, indent + "    ", v.vals[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_ROSTOPIC_MESSAGE_ARRAYVAL_H
