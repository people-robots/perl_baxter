; Auto-generated. Do not edit!


(cl:in-package cob_people_detection-msg)


;//! \htmlinclude deleteDataResult.msg.html

(cl:defclass <deleteDataResult> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass deleteDataResult (<deleteDataResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <deleteDataResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'deleteDataResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cob_people_detection-msg:<deleteDataResult> is deprecated: use cob_people_detection-msg:deleteDataResult instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <deleteDataResult>) ostream)
  "Serializes a message object of type '<deleteDataResult>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <deleteDataResult>) istream)
  "Deserializes a message object of type '<deleteDataResult>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<deleteDataResult>)))
  "Returns string type for a message object of type '<deleteDataResult>"
  "cob_people_detection/deleteDataResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'deleteDataResult)))
  "Returns string type for a message object of type 'deleteDataResult"
  "cob_people_detection/deleteDataResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<deleteDataResult>)))
  "Returns md5sum for a message object of type '<deleteDataResult>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'deleteDataResult)))
  "Returns md5sum for a message object of type 'deleteDataResult"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<deleteDataResult>)))
  "Returns full string definition for message of type '<deleteDataResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# result message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'deleteDataResult)))
  "Returns full string definition for message of type 'deleteDataResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# result message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <deleteDataResult>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <deleteDataResult>))
  "Converts a ROS message object to a list"
  (cl:list 'deleteDataResult
))