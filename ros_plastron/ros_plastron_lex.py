import ply.lex as lex

import sys

#Implementation of lecal analyzer

#Create Tokens

keywords = {
    'subscribe': 'SUBSCRIBE',
    'unsubscribe': 'UNSUBSCRIBE',
    'service': 'SERVICE',
    'client': 'CLIENT',
    'node': 'NODE',
    'nodelet': 'NODELET',
    'create_node': 'CREATE_NODE',
    'create_nodelet': 'CREATE_NODELET',
    'load': 'LOAD',
    'publish': 'PUBLISH',
    'create_msgs': 'CREATE_MSGS',
    'generate_launch': 'GENERATE_LAUNCH',
    'empty': 'EMPTY',
    'subscriber': 'SUBSCRIBER',
    'server': 'SERVER',
}

tokens = [
    'NAME',
    'EQUALS',
    'COMMA',
    'INT',
    'LEFT_P',
    'RIGHT_P',
    'STRING_LITERAL',
    'CHAR_LITERAL',
    'DOT',
] + list(keywords.values())

t_EQUALS = r'\='
t_DOT = r'\.'
t_LEFT_P = r'\('
t_RIGHT_P = r'\)'
t_COMMA = r'\,'

t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
t_CHAR_LITERAL = r'\'([^\\\n]|(\\.))*?\''

t_ignore_COMMENT = '//.*'
t_ignore = ' \t\n'

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'NAME')
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_BLOCK_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
