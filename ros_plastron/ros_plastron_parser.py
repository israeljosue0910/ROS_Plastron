import ply.yacc as yacc
from ros_plastron import ros_plastron_lex


tokens = ros_plastron_lex.tokens

variables = {}

def p_def(p):
    '''
    def : NAME EQUALS STRING_LITERAL
        | NAME EQUALS INT
        | NAME EQUALS CHAR_LITERAL
        | NAME EQUALS NAME
        | NAME EQUALS func
        | NAME EQUALS NAME DOT mod
    '''
    variables[p[1]] = p[3]

def p_func(p):
    '''
    func  : prim_f paren
    '''
    p[0] = (p[1], p[2])

def p_var_mod(p):
    '''
    var_mod  : NAME DOT mod
    '''
    p[0] = (p[1], p[2])

def p_mod(p):
    '''
    mod  : prim_m paren
    '''
    p[0] = (p[1], p[2])

def p_prim_f(p):
    '''
    prim_f  : CREATE_NODE
            | CREATE_MSGS
            | LOAD
            | GENERATE_LAUNCH
            | CREATE_NODELET
    '''
    p[0] = p[1]

def p_exp(p):
    '''
    exp : def
        | func
        | var_mod
    '''
    p[0] = p[1]

def p_prim_m(p):
    '''
    prim_m  : PUBLISH
            | SUBSCRIBE
            | UNSUBSCRIBE
            | SERVICE
            | CLIENT
    '''
    p[0] = p[1]

def p_paren(p):
    '''
    paren   : paren1
            | paren2
    '''
    p[0] = p[1]

def p_paren1(p):
    '''
    paren1  : LEFT_P NAME COMMA STRING_LITERAL RIGHT_P
            | LEFT_P STRING_LITERAL COMMA communication RIGHT_P
    '''
    p[0] = (p[2], p[4])

def p_paren2(p):
    '''
    paren2  : LEFT_P STRING_LITERAL RIGHT_P
            | LEFT_P EMPTY RIGHT_P
    '''
    p[0] = p[2]

def p_communication(p):
    '''
    communication   : SUBSCRIBER
                    | SERVER
    '''
    p[0] = p[1]

yacc.yacc()

data = "node_test = create_node(\"foo\")"

yacc.parse(data)