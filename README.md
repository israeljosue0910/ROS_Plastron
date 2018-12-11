
### **Robotics Operating System**
---
The Robot Operating System (ROS) is a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robotic platforms. 

### **About**
---
ROS_Plastron is a language that aims to make the Robotic Operating System more accessible for users who have no previous programming experience. Its main features allow users to start their robotics project with basic ROS Node templates that they can modify to their needs, as well as manipulating their existing ROS Nodes.

### **Language Features**
---
ROS_Plastron currently supports two features: Node Creation and Existing Node Manipulation. The Node Creation feature allows users to generate four types of node templates: Subscribers, Publishers, Clients and Servers. The Existing Node Manipulation feature allows users to load existing node files into the system, perform changes to it (i.e unsubscribing a node from a topic and subscribing it to another topic) and then generate the node file. In the future ROS_Plastron will support other features like: Custom Message Creation and URDF Files Creation.

### **Sample Codes**
---
#### Example 1: Creating a Publisher Node
```
create_node 'publisher' as node1
create_message msg1 of message_type Point and input 5,6,7
create_message msg2 of message_type Vector3 and input 1,3,0
create_message msg3 of message_type String and input "hello_World"
create_message msg4 of message_type Quaternion and input 8,9,10,11
create_message msg5 of message_type Pose2D and input 1,2,80
node1 publish msg1 to 'chatter' of message_type Point
node1 publish msg2 to 'chatter1' of message_type Vector3
node1 publish msg3 to 'chatter2' of message_type String
node1 publish msg4 to 'chatter3' of message_type Quaternion
node1 publish msg5 to 'chatter4' of message_type Pose2D
generate_node node1
```
#### Example 2: Creating a Subscriber Node
```
create_node 'subscriber' as node2
subscribe node2 to 'chatter' of message_type String
generate_node node2
```
#### Example 3: Creating a Client Node
```
create_node 'client' as node3
node3 client_requests 'add_two_ints' of service_type AddTwoInts with input 5,6
node3 client_requests 'waypoint_clear' of service_type WaypointClear with input none
node3 client_requests 'set_bool' of service_type SetBool with input True
generate_node node3
```
#### Example 4: Creating a Server Node
```
create_node 'server' as node4
node4 provides_service 'add_two_ints' of service_type AddTwoInts
node4 provides_service 'waypoint_clear' of service_type WaypointClear
node4 provides_service 'set_bool' of service_type SetBool
generate_node node4
```
#### Example 5: Loading and modifying a node
```
load subscriber_sub1 as node5
unsubscribe node5 from 'chatter'
subscribe node5 to 'topic_added_after_load' of message_type String
generate_node node5
```

### **Video Tutorial**
---
<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/mOqia0bzEIw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### **Install**
---
#### Dependencies
The project utilizes Python 3.4 or higher with the PLY package.

#### Instructions
* Download <a href="https://github.com/israeljosue0910/ROS_Plastron/archive/master.zip"> ROS_Plastron </a>
* Install Python 3.4 and the PLY package.
* Run ROS_Plastron/src/main.py

### **Final Report**
---
View <a href="https://github.com/israeljosue0910/ROS_Plastron/archive/master.zip"> Final Report </a>

