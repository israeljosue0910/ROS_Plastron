
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDTWOINTS AND AS CHAR CLIENT_REQUESTS COMMA CREATE_MESSAGE CREATE_NODE EMPTY FALSE FLOAT32 FROM GENERATE_NODE INPUT INT INT32 LOAD MESSAGE_TYPE NAME NONE OF POINT POSE2D PROVIDES_SERVICE PUBLISH QUATERNION SERVICE_TYPE SETBOOL STOP_PUBLISHING STOP_REQUEST STOP_SERVICE STRING STRING_LITERAL SUBSCRIBE TO TOPIC_SERVICE TRIGGER TRUE UNSUBSCRIBE VECTOR3 WAYPOINTCLEAR WAYPOINTPULL WITH WORDCOUNT\n    exp : node_mod\n        | unsub\n        | stop_pub\n        | pub\n        | sub\n        | stop_serv\n        | serv\n        | stop_clnt\n        | clnt\n        | message\n    \n   sub : SUBSCRIBE NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type\n   \n   unsub : UNSUBSCRIBE NAME FROM TOPIC_SERVICE\n   \n   pub : NAME PUBLISH NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type\n   \n   stop_pub : NAME STOP_PUBLISHING TO TOPIC_SERVICE\n   \n   serv : NAME PROVIDES_SERVICE TOPIC_SERVICE OF SERVICE_TYPE serv_type\n   \n   stop_serv : NAME STOP_SERVICE TOPIC_SERVICE\n   \n   clnt : NAME CLIENT_REQUESTS TOPIC_SERVICE OF SERVICE_TYPE serv_type WITH INPUT params\n   \n   stop_clnt : NAME STOP_REQUEST TOPIC_SERVICE\n   \n   params : NONE\n        | list\n   \n    list : term\n        | list COMMA term\n    \n    term : INT\n        | STRING_LITERAL\n        | TRUE\n        | FALSE\n    \n   node_mod : CREATE_NODE TOPIC_SERVICE AS NAME\n        | GENERATE_NODE NAME\n        | LOAD NAME AS NAME\n   \n   message : CREATE_MESSAGE NAME OF MESSAGE_TYPE sub_type AND INPUT list\n   \n   serv_type : ADDTWOINTS\n        | EMPTY\n        | SETBOOL\n        | TRIGGER\n        | WAYPOINTCLEAR\n        | WAYPOINTPULL\n        | WORDCOUNT\n   \n   sub_type : STRING\n        | QUATERNION\n        | POINT\n        | POSE2D\n        | VECTOR3\n        | CHAR\n        | INT32\n        | FLOAT32\n   '
    
_lr_action_items = {'CREATE_NODE':([0,],[12,]),'GENERATE_NODE':([0,],[14,]),'LOAD':([0,],[15,]),'UNSUBSCRIBE':([0,],[16,]),'NAME':([0,14,15,16,17,18,21,31,38,],[13,26,27,28,29,30,33,42,47,]),'SUBSCRIBE':([0,],[17,]),'CREATE_MESSAGE':([0,],[18,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,26,34,36,42,43,47,48,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,78,80,82,83,84,85,86,87,88,89,90,92,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-28,-16,-18,-27,-14,-29,-12,-38,-39,-40,-41,-42,-43,-44,-45,-15,-31,-32,-33,-34,-35,-36,-37,-11,-13,-30,-21,-23,-24,-25,-26,-17,-19,-20,-22,]),'TOPIC_SERVICE':([12,22,23,24,25,32,39,40,44,],[19,34,35,36,37,43,48,49,51,]),'STOP_PUBLISHING':([13,],[20,]),'PUBLISH':([13,],[21,]),'STOP_SERVICE':([13,],[22,]),'PROVIDES_SERVICE':([13,],[23,]),'STOP_REQUEST':([13,],[24,]),'CLIENT_REQUESTS':([13,],[25,]),'AS':([19,27,],[31,38,]),'TO':([20,29,33,],[32,40,44,]),'FROM':([28,],[39,]),'OF':([30,35,37,49,51,],[41,45,46,54,64,]),'MESSAGE_TYPE':([41,54,64,],[50,74,76,]),'SERVICE_TYPE':([45,46,],[52,53,]),'STRING':([50,74,76,],[56,56,56,]),'QUATERNION':([50,74,76,],[57,57,57,]),'POINT':([50,74,76,],[58,58,58,]),'POSE2D':([50,74,76,],[59,59,59,]),'VECTOR3':([50,74,76,],[60,60,60,]),'CHAR':([50,74,76,],[61,61,61,]),'INT32':([50,74,76,],[62,62,62,]),'FLOAT32':([50,74,76,],[63,63,63,]),'ADDTWOINTS':([52,53,],[66,66,]),'EMPTY':([52,53,],[67,67,]),'SETBOOL':([52,53,],[68,68,]),'TRIGGER':([52,53,],[69,69,]),'WAYPOINTCLEAR':([52,53,],[70,70,]),'WAYPOINTPULL':([52,53,],[71,71,]),'WORDCOUNT':([52,53,],[72,72,]),'AND':([55,56,57,58,59,60,61,62,63,],[75,-38,-39,-40,-41,-42,-43,-44,-45,]),'WITH':([66,67,68,69,70,71,72,73,],[-31,-32,-33,-34,-35,-36,-37,77,]),'INPUT':([75,77,],[79,81,]),'INT':([79,81,91,],[84,84,84,]),'STRING_LITERAL':([79,81,91,],[85,85,85,]),'TRUE':([79,81,91,],[86,86,86,]),'FALSE':([79,81,91,],[87,87,87,]),'NONE':([81,],[89,]),'COMMA':([82,83,84,85,86,87,90,92,],[91,-21,-23,-24,-25,-26,91,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,],[1,]),'node_mod':([0,],[2,]),'unsub':([0,],[3,]),'stop_pub':([0,],[4,]),'pub':([0,],[5,]),'sub':([0,],[6,]),'stop_serv':([0,],[7,]),'serv':([0,],[8,]),'stop_clnt':([0,],[9,]),'clnt':([0,],[10,]),'message':([0,],[11,]),'sub_type':([50,74,76,],[55,78,80,]),'serv_type':([52,53,],[65,73,]),'list':([79,81,],[82,90,]),'term':([79,81,91,],[83,83,92,]),'params':([81,],[88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> node_mod','exp',1,'p_exp','plastron_parser.py',25),
  ('exp -> unsub','exp',1,'p_exp','plastron_parser.py',26),
  ('exp -> stop_pub','exp',1,'p_exp','plastron_parser.py',27),
  ('exp -> pub','exp',1,'p_exp','plastron_parser.py',28),
  ('exp -> sub','exp',1,'p_exp','plastron_parser.py',29),
  ('exp -> stop_serv','exp',1,'p_exp','plastron_parser.py',30),
  ('exp -> serv','exp',1,'p_exp','plastron_parser.py',31),
  ('exp -> stop_clnt','exp',1,'p_exp','plastron_parser.py',32),
  ('exp -> clnt','exp',1,'p_exp','plastron_parser.py',33),
  ('exp -> message','exp',1,'p_exp','plastron_parser.py',34),
  ('sub -> SUBSCRIBE NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type','sub',7,'p_sub','plastron_parser.py',40),
  ('unsub -> UNSUBSCRIBE NAME FROM TOPIC_SERVICE','unsub',4,'p_unsub','plastron_parser.py',59),
  ('pub -> NAME PUBLISH NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type','pub',8,'p_pub','plastron_parser.py',78),
  ('stop_pub -> NAME STOP_PUBLISHING TO TOPIC_SERVICE','stop_pub',4,'p_stop_pub','plastron_parser.py',103),
  ('serv -> NAME PROVIDES_SERVICE TOPIC_SERVICE OF SERVICE_TYPE serv_type','serv',6,'p_serv','plastron_parser.py',124),
  ('stop_serv -> NAME STOP_SERVICE TOPIC_SERVICE','stop_serv',3,'p_stop_serv','plastron_parser.py',144),
  ('clnt -> NAME CLIENT_REQUESTS TOPIC_SERVICE OF SERVICE_TYPE serv_type WITH INPUT params','clnt',9,'p_clnt','plastron_parser.py',163),
  ('stop_clnt -> NAME STOP_REQUEST TOPIC_SERVICE','stop_clnt',3,'p_stop_clnt','plastron_parser.py',185),
  ('params -> NONE','params',1,'p_params','plastron_parser.py',206),
  ('params -> list','params',1,'p_params','plastron_parser.py',207),
  ('list -> term','list',1,'p_list','plastron_parser.py',214),
  ('list -> list COMMA term','list',3,'p_list','plastron_parser.py',215),
  ('term -> INT','term',1,'p_term','plastron_parser.py',225),
  ('term -> STRING_LITERAL','term',1,'p_term','plastron_parser.py',226),
  ('term -> TRUE','term',1,'p_term','plastron_parser.py',227),
  ('term -> FALSE','term',1,'p_term','plastron_parser.py',228),
  ('node_mod -> CREATE_NODE TOPIC_SERVICE AS NAME','node_mod',4,'p_node_mod','plastron_parser.py',235),
  ('node_mod -> GENERATE_NODE NAME','node_mod',2,'p_node_mod','plastron_parser.py',236),
  ('node_mod -> LOAD NAME AS NAME','node_mod',4,'p_node_mod','plastron_parser.py',237),
  ('message -> CREATE_MESSAGE NAME OF MESSAGE_TYPE sub_type AND INPUT list','message',8,'p_message','plastron_parser.py',280),
  ('serv_type -> ADDTWOINTS','serv_type',1,'p_serv_type','plastron_parser.py',297),
  ('serv_type -> EMPTY','serv_type',1,'p_serv_type','plastron_parser.py',298),
  ('serv_type -> SETBOOL','serv_type',1,'p_serv_type','plastron_parser.py',299),
  ('serv_type -> TRIGGER','serv_type',1,'p_serv_type','plastron_parser.py',300),
  ('serv_type -> WAYPOINTCLEAR','serv_type',1,'p_serv_type','plastron_parser.py',301),
  ('serv_type -> WAYPOINTPULL','serv_type',1,'p_serv_type','plastron_parser.py',302),
  ('serv_type -> WORDCOUNT','serv_type',1,'p_serv_type','plastron_parser.py',303),
  ('sub_type -> STRING','sub_type',1,'p_sub_type','plastron_parser.py',310),
  ('sub_type -> QUATERNION','sub_type',1,'p_sub_type','plastron_parser.py',311),
  ('sub_type -> POINT','sub_type',1,'p_sub_type','plastron_parser.py',312),
  ('sub_type -> POSE2D','sub_type',1,'p_sub_type','plastron_parser.py',313),
  ('sub_type -> VECTOR3','sub_type',1,'p_sub_type','plastron_parser.py',314),
  ('sub_type -> CHAR','sub_type',1,'p_sub_type','plastron_parser.py',315),
  ('sub_type -> INT32','sub_type',1,'p_sub_type','plastron_parser.py',316),
  ('sub_type -> FLOAT32','sub_type',1,'p_sub_type','plastron_parser.py',317),
]
