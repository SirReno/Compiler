
# -----------------------------------------------------------------------------
# Typescript
# Rodolfo Rincón Muñoz A01206310    
# -----------------------------------------------------------------------------
#from __future__ import annotations
import ply.lex as lex
import ply.yacc as yacc
import re
from node import *

# TOKENS
tokens = [
    # IDENTIFIERS
    'ID',
    # LITERALS
    'LIT_NUMBER',
    'LIT_STRING',
    # SYMBOLS
    'CURLYLEFT',
    'CURLYRIGHT',
    'LPAREN',
    'RPAREN',
    'SEMI_COLON',
    # COMMENTS
    # 'MULTI_COM',
    # 'SINGLE_COM',
    # OPERATORS
    'OP_AND',
    'OP_OR',
    'OP_TYPE_ASSIGN',
    'OP_VALUE_ASSIGN',
    'OP_DIVIDE',
    'OP_LESS_OR_EQUAL',
    'OP_LESS_THAN',
    'OP_MINUS',
    'OP_MOD',
    'OP_MORE_OR_EQUAL',
    'OP_MORE_THAN',
    'OP_MULT',
    'OP_NOT',
    'OP_NOT_EQUALS',
    'OP_EQUALS',
    'OP_PLUS',
]

# RESERVED WORD LIST
reserved = {
    'boolean': 'BOOL',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'readline': 'READ',
    'printline': 'PRINT',
    'const': 'CONST',
    'else': 'ELSE',
    'function' : 'FUNCTION',
    'if': 'IF',
    'let': 'LET',
    'number': 'NUMBER',
    'return': 'RETURN',
    'string': 'STRING',
    'while': 'WHILE',
}

tokens = tokens + list(reserved.values())

# COMMENTS
def t_SINGLE_COM(t):
    r'//.*$'
    pass


def t_MULTI_COM(t):
    r'/[*][^*]*[*]+([^/*][^*]*[*]+)*/|//[^\n]*'
    pass


# REGULAR EXPRESSIONS
# OPERATORS
t_OP_AND = r'\&\&'
t_OP_OR = r'\|\|'
t_OP_TYPE_ASSIGN = r'\:'
t_OP_VALUE_ASSIGN = r'\='
t_OP_DIVIDE = r'/'
t_OP_LESS_OR_EQUAL = r'\<\='
t_OP_LESS_THAN = r'\<'
t_OP_MINUS = r'\-'
t_OP_MOD = r'(MOD|mod)'
t_OP_MORE_OR_EQUAL = r'\>\='
t_OP_MORE_THAN = r'\>'
t_OP_MULT = r'\*'
t_OP_NOT = r'(NOT|not)'
t_OP_NOT_EQUALS = r'\!\='
t_OP_EQUALS = r'\=\='
t_OP_PLUS = r'\+'


# SYMBOLS
t_CURLYLEFT = r'\{'
t_CURLYRIGHT= r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI_COLON = r'\;'

# KEYWORDS
t_BOOL = r'(Boolean)'
t_CONST = r'(CONST|const)'
t_READ = r'(READ|read)'
t_PRINT = r'(PRINT|print)'
t_ELSE = r'(ELSE|else)'
t_IF = r'(IF|if)'
t_LET= r'(LET|let)'
t_STRING = r'(String)'
t_WHILE = r'(WHILE|while)'

# IGNORED CHARACTERS I.E WHITESPACE
t_ignore_space = r'\ '
t_ignore_newline = r'\n'
t_ignore_tab = r'\t'
t_ignore_vcmd = r'\v'

# IDENTIFIERS
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, "ID")
    return t

# LITERALS
# t_LIT_BOOL = r'(true|TRUE)|(false|FALSE)'
t_LIT_NUMBER = r'([0-9]*\.?[0-9]+)'
t_LIT_STRING = r'(?:\'(?:[^\']+|\'\')*\'|\"(?:[^"]+|\"\")*\")'


# ERROR HANDLING OF ILLEGAL CHARACTERS
def t_error(t):
    print("Illegal character: '%s' encountered" % t.value[0])
    t.lexer.skip(1)


def p_program(p):
    '''
    program : statement program    
            | statement
    '''
    if(len(p) == 2):
        p[0] = Node('Program', None, None, [p[1]])
    else:
        p[0] = Node('Program', None, None, [p[1],p[2]])

def p_statement(p):
    '''
    statement : var_declaration
              | const_declaration
              | if_statement
              | while_statement
              | input_statement
              | output_statement
              | function_statement
    '''
    p[0] = Node('Statement', None, None, [p[1]])


def p_var_declaration(p):
    '''
    var_declaration : LET ID OP_TYPE_ASSIGN type OP_VALUE_ASSIGN expression SEMI_COLON
    '''
    p[0] = Node('Var_Declaration', None, None, [p[4], p[6]])

def p_const_declaration(p):
    '''
    const_declaration : CONST ID OP_TYPE_ASSIGN type OP_VALUE_ASSIGN expression SEMI_COLON
    '''
    p[0] = Node('Const_Declaration', None, None, [p[4], p[6]])

def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT
                 | IF LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT ELSE CURLYLEFT program CURLYRIGHT 
    '''
    if(len(p) == 8):
        p[0] = Node('If_Statement', None, None, [p[3], p[6]])
    else:
        p[0] = Node('If_Statement', None, None, [p[3], p[6], p[10]])

def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT
    '''
    p[0] = Node('While_statement', None, None, [p[3], p[6]])

def p_input_statement(p):
    '''
    input_statement : READ LPAREN RPAREN SEMI_COLON
    '''
    p[0] = Node('Input_Statement', None, None, None)

def p_output_statement(p):
    '''
    output_statement : PRINT LPAREN expression RPAREN SEMI_COLON
    '''
    p[0] = Node('Output_Statement', None, None, [p[3]])

def p_function_statement(p):
    '''
    function_statement : FUNCTION ID LPAREN RPAREN CURLYLEFT statement RETURN expression SEMI_COLON CURLYRIGHT
    '''

def p_type(p):
    '''
    type : NUMBER
         | BOOL
         | STRING
    '''
    p[0] = Node('Type', None, None, [p[1]])

def p_expression(p):
    '''
    expression : simple_expression
               | OP_MINUS simple_expression
               | logic_expression
    '''
    if(len(p) == 2):
        p[0] = Node('Expression', None, None, [p[1]])
    else:
        p[0] = Node('Expression', None, None, [p[2]])

def p_simple_expression(p):
    '''
    simple_expression : term OP_PLUS simple_expression
                      | term OP_MINUS simple_expression
                      | term
    '''
    if(len(p) == 4):
        p[0] = Node('Simple_expression', None, None, [p[1], p[3]])
    else:
        p[0] = Node('Simple_expression', None, None, [p[1]])

def p_logic_expression(p):
    '''
    logic_expression : simple_expression logical_op simple_expression
                     | OP_NOT logic_expression
    '''
    if(len(p) == 4):
        p[0] = Node('Logic_Expression', None, None, [p[1], p[2], p[3]])
    else:
        p[0] = Node('Logic_Expression', None, None, [p[2]])

def p_term(p):
    '''
    term : factor OP_MULT term
         | factor OP_DIVIDE term
         | factor OP_MOD term
         | factor
    '''
    if(len(p) == 4):
        p[0] = Node('Term', None, None, [p[1], p[3]])
    else:
        p[0] = Node('Term', None, None, [p[1]])

def p_factor(p):
    '''
    factor : lit_value
           | LPAREN expression RPAREN
           | ID
    '''
    if(len(p) == 4):
        p[0] = Node('Factor', None, None, [p[2]])
    elif(p[1] == 'ID'):
        p[0] = Node('Factor', None, None, [p[1]])
    else:
        p[0] = Node('Factor', None, None, [p[1]])

def p_logical_op(p):
    '''
    logical_op : OP_AND
                  | OP_OR
                  | OP_MORE_OR_EQUAL
                  | OP_LESS_OR_EQUAL
                  | OP_MORE_THAN
                  | OP_LESS_THAN
                  | OP_NOT_EQUALS
                  | OP_EQUALS
    '''
    p[0] = Node('Logical_Operator', None, None, [p[1]])

def p_lit_value(p):
    '''
    lit_value : TRUE
              | FALSE
              | LIT_NUMBER
              | LIT_STRING
    '''
    p[0] = Node('Lit_value', None, None, [p[1]])

def p_error(p):
    if(str(p)!='None'):
        print("\nSYNTAX ERROR '%s'" % (str(p)))

# Build the parser


#TEST 1
print("BEGGINING OF TEST 1")
with open('./tests/test1.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST1.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 1\n\n")

#TEST 2
print("BEGGINING OF TEST 2")
with open('./tests/test2.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST2.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 2\n\n")

#TEST 3
print("BEGGINING OF TEST 3")
with open('./tests/test3.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    # Read TOKENS
    lexer.input(data)
    # BUILD THE PARSER
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    # Parses Grammar
    res = parser.parse(data)
    r = open("AST3.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 3\n\n")

#TEST 4
print("BEGGINING OF TEST 4")
with open('./tests/test4.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST4.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 4\n\n")

#TEST 5
print("BEGGINING OF TEST 5")
with open('./tests/test5.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST5.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 5\n\n")

#TEST 6
print("BEGGINING OF TEST 6")
with open('./tests/test6.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST6.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 6\n\n")

#TEST 7
print("BEGGINING OF TEST 7")
with open('./tests/test7.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST7.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 7\n\n")

#TEST 8
print("BEGGINING OF TEST 8")
with open('./tests/test8.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST8.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 8\n\n")


#TEST 9
print("BEGGINING OF TEST 9")
with open('./tests/test9.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("AST9.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST 9\n\n")

#TEST incorrect 1 
print("BEGGINING OF TEST with errors 1")
with open('./tests/itest1.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("ASTi1.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST with errors 1\n\n")

#TEST incorrect 2
print("BEGGINING OF TEST with errors 2")
with open('./tests/itest2.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("ASTi2.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST with errors 2\n\n")

#TEST incorrect 3
print("BEGGINING OF TEST with errors 3")
with open('./tests/itest3.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("ASTi3.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST with errors 3 \n\n")

#TEST incorrect 4
print("BEGGINING OF TEST with errors 3")
with open('./tests/itest4.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("ASTi4.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST with errors 4 \n\n")

#TEST incorrect 5
print("BEGGINING OF TEST with errors 5")
with open('./tests/itest5.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("ASTi5.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST with errors 5 \n\n")

#TEST incorrect 6
print("BEGGINING OF TEST with errors 6")
with open('./tests/itest6.ts', 'r') as file:
    data = file.read()
    # BUILD THE LEXER
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()

    print(data)

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
    res = parser.parse(data)
    r = open("ASTi6.txt", "w+")
    r.write(str(res))
    r.close()
    print('Árbol generado en AST.txt')
print("END OF TEST with errors 6 \n\n")









