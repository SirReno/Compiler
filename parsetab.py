
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL CONST CURLYLEFT CURLYRIGHT ELSE FALSE FUNCTION ID IF LET LIT_NUMBER LIT_STRING LPAREN NUMBER OP_AND OP_DIVIDE OP_EQUALS OP_LESS_OR_EQUAL OP_LESS_THAN OP_MINUS OP_MOD OP_MORE_OR_EQUAL OP_MORE_THAN OP_MULT OP_NOT OP_NOT_EQUALS OP_OR OP_PLUS OP_TYPE_ASSIGN OP_VALUE_ASSIGN PRINT READ RETURN RPAREN SEMI_COLON STRING TRUE WHILE\n    program : statement program    \n            | statement\n    \n    statement : var_declaration\n              | const_declaration\n              | if_statement\n              | while_statement\n              | input_statement\n              | output_statement\n              | function_statement\n    \n    var_declaration : LET ID OP_TYPE_ASSIGN type OP_VALUE_ASSIGN expression SEMI_COLON\n    \n    const_declaration : CONST ID OP_TYPE_ASSIGN type OP_VALUE_ASSIGN expression SEMI_COLON\n    \n    if_statement : IF LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT\n                 | IF LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT ELSE CURLYLEFT program CURLYRIGHT \n    \n    while_statement : WHILE LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT\n    \n    input_statement : READ LPAREN RPAREN SEMI_COLON\n    \n    output_statement : PRINT LPAREN expression RPAREN SEMI_COLON\n    \n    function_statement : FUNCTION ID LPAREN RPAREN CURLYLEFT statement RETURN expression SEMI_COLON CURLYRIGHT\n    \n    type : NUMBER\n         | BOOL\n         | STRING\n    \n    expression : simple_expression\n               | OP_MINUS simple_expression\n               | logic_expression\n    \n    simple_expression : term OP_PLUS simple_expression\n                      | term OP_MINUS simple_expression\n                      | term\n    \n    logic_expression : simple_expression logical_op simple_expression\n                     | OP_NOT logic_expression\n    \n    term : factor OP_MULT term\n         | factor OP_DIVIDE term\n         | factor OP_MOD term\n         | factor\n    \n    factor : lit_value\n           | LPAREN expression RPAREN\n           | ID\n    \n    logical_op : OP_AND\n                  | OP_OR\n                  | OP_MORE_OR_EQUAL\n                  | OP_LESS_OR_EQUAL\n                  | OP_MORE_THAN\n                  | OP_LESS_THAN\n                  | OP_NOT_EQUALS\n                  | OP_EQUALS\n    \n    lit_value : TRUE\n              | FALSE\n              | LIT_NUMBER\n              | LIT_STRING\n    '
    
_lr_action_items = {'LET':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[10,10,-3,-4,-5,-6,-7,-8,-9,-15,10,10,-16,10,-10,-11,-12,-14,10,-17,-13,]),'CONST':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[11,11,-3,-4,-5,-6,-7,-8,-9,-15,11,11,-16,11,-10,-11,-12,-14,11,-17,-13,]),'IF':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[12,12,-3,-4,-5,-6,-7,-8,-9,-15,12,12,-16,12,-10,-11,-12,-14,12,-17,-13,]),'WHILE':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[13,13,-3,-4,-5,-6,-7,-8,-9,-15,13,13,-16,13,-10,-11,-12,-14,13,-17,-13,]),'READ':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[14,14,-3,-4,-5,-6,-7,-8,-9,-15,14,14,-16,14,-10,-11,-12,-14,14,-17,-13,]),'PRINT':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[15,15,-3,-4,-5,-6,-7,-8,-9,-15,15,15,-16,15,-10,-11,-12,-14,15,-17,-13,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,70,76,83,84,85,91,92,93,94,98,101,102,],[16,16,-3,-4,-5,-6,-7,-8,-9,-15,16,16,-16,16,-10,-11,-12,-14,16,-17,-13,]),'$end':([1,2,3,4,5,6,7,8,9,17,70,84,91,92,93,94,101,102,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-1,-15,-16,-10,-11,-12,-14,-17,-13,]),'CURLYRIGHT':([2,3,4,5,6,7,8,9,17,70,84,88,89,91,92,93,94,99,100,101,102,],[-2,-3,-4,-5,-6,-7,-8,-9,-1,-15,-16,93,94,-10,-11,-12,-14,101,102,-17,-13,]),'RETURN':([3,4,5,6,7,8,9,70,84,90,91,92,93,94,101,102,],[-3,-4,-5,-6,-7,-8,-9,-15,-16,95,-10,-11,-12,-14,-17,-13,]),'ID':([10,11,16,20,21,23,27,30,33,52,53,54,55,56,57,58,59,60,62,63,66,67,68,73,74,95,],[18,19,24,36,36,36,36,36,36,36,-36,-37,-38,-39,-40,-41,-42,-43,36,36,36,36,36,36,36,36,]),'LPAREN':([12,13,14,15,20,21,23,24,27,30,33,52,53,54,55,56,57,58,59,60,62,63,66,67,68,73,74,95,],[20,21,22,23,27,27,27,44,27,27,27,27,-36,-37,-38,-39,-40,-41,-42,-43,27,27,27,27,27,27,27,27,]),'OP_TYPE_ASSIGN':([18,19,],[25,26,]),'OP_MINUS':([20,21,23,27,32,34,35,36,37,38,39,40,73,74,75,80,81,82,95,],[30,30,30,30,63,-32,-33,-35,-44,-45,-46,-47,30,30,-34,-29,-30,-31,30,]),'OP_NOT':([20,21,23,27,33,73,74,95,],[33,33,33,33,33,33,33,33,]),'TRUE':([20,21,23,27,30,33,52,53,54,55,56,57,58,59,60,62,63,66,67,68,73,74,95,],[37,37,37,37,37,37,37,-36,-37,-38,-39,-40,-41,-42,-43,37,37,37,37,37,37,37,37,]),'FALSE':([20,21,23,27,30,33,52,53,54,55,56,57,58,59,60,62,63,66,67,68,73,74,95,],[38,38,38,38,38,38,38,-36,-37,-38,-39,-40,-41,-42,-43,38,38,38,38,38,38,38,38,]),'LIT_NUMBER':([20,21,23,27,30,33,52,53,54,55,56,57,58,59,60,62,63,66,67,68,73,74,95,],[39,39,39,39,39,39,39,-36,-37,-38,-39,-40,-41,-42,-43,39,39,39,39,39,39,39,39,]),'LIT_STRING':([20,21,23,27,30,33,52,53,54,55,56,57,58,59,60,62,63,66,67,68,73,74,95,],[40,40,40,40,40,40,40,-36,-37,-38,-39,-40,-41,-42,-43,40,40,40,40,40,40,40,40,]),'RPAREN':([22,28,29,31,32,34,35,36,37,38,39,40,41,43,44,50,61,64,75,77,78,79,80,81,82,],[42,51,-21,-23,-26,-32,-33,-35,-44,-45,-46,-47,69,71,72,75,-22,-28,-34,-27,-24,-25,-29,-30,-31,]),'NUMBER':([25,26,],[46,46,]),'BOOL':([25,26,],[47,47,]),'STRING':([25,26,],[48,48,]),'SEMI_COLON':([29,31,32,34,35,36,37,38,39,40,42,61,64,71,75,77,78,79,80,81,82,86,87,97,],[-21,-23,-26,-32,-33,-35,-44,-45,-46,-47,70,-22,-28,84,-34,-27,-24,-25,-29,-30,-31,91,92,99,]),'OP_AND':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[53,-26,-32,-33,-35,-44,-45,-46,-47,53,-34,-24,-25,-29,-30,-31,]),'OP_OR':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[54,-26,-32,-33,-35,-44,-45,-46,-47,54,-34,-24,-25,-29,-30,-31,]),'OP_MORE_OR_EQUAL':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[55,-26,-32,-33,-35,-44,-45,-46,-47,55,-34,-24,-25,-29,-30,-31,]),'OP_LESS_OR_EQUAL':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[56,-26,-32,-33,-35,-44,-45,-46,-47,56,-34,-24,-25,-29,-30,-31,]),'OP_MORE_THAN':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[57,-26,-32,-33,-35,-44,-45,-46,-47,57,-34,-24,-25,-29,-30,-31,]),'OP_LESS_THAN':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[58,-26,-32,-33,-35,-44,-45,-46,-47,58,-34,-24,-25,-29,-30,-31,]),'OP_NOT_EQUALS':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[59,-26,-32,-33,-35,-44,-45,-46,-47,59,-34,-24,-25,-29,-30,-31,]),'OP_EQUALS':([29,32,34,35,36,37,38,39,40,65,75,78,79,80,81,82,],[60,-26,-32,-33,-35,-44,-45,-46,-47,60,-34,-24,-25,-29,-30,-31,]),'OP_PLUS':([32,34,35,36,37,38,39,40,75,80,81,82,],[62,-32,-33,-35,-44,-45,-46,-47,-34,-29,-30,-31,]),'OP_MULT':([34,35,36,37,38,39,40,75,],[66,-33,-35,-44,-45,-46,-47,-34,]),'OP_DIVIDE':([34,35,36,37,38,39,40,75,],[67,-33,-35,-44,-45,-46,-47,-34,]),'OP_MOD':([34,35,36,37,38,39,40,75,],[68,-33,-35,-44,-45,-46,-47,-34,]),'OP_VALUE_ASSIGN':([45,46,47,48,49,],[73,-18,-19,-20,74,]),'CURLYLEFT':([51,69,72,96,],[76,83,85,98,]),'ELSE':([93,],[96,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,76,83,98,],[1,17,88,89,100,]),'statement':([0,2,76,83,85,98,],[2,2,2,2,90,2,]),'var_declaration':([0,2,76,83,85,98,],[3,3,3,3,3,3,]),'const_declaration':([0,2,76,83,85,98,],[4,4,4,4,4,4,]),'if_statement':([0,2,76,83,85,98,],[5,5,5,5,5,5,]),'while_statement':([0,2,76,83,85,98,],[6,6,6,6,6,6,]),'input_statement':([0,2,76,83,85,98,],[7,7,7,7,7,7,]),'output_statement':([0,2,76,83,85,98,],[8,8,8,8,8,8,]),'function_statement':([0,2,76,83,85,98,],[9,9,9,9,9,9,]),'expression':([20,21,23,27,73,74,95,],[28,41,43,50,86,87,97,]),'simple_expression':([20,21,23,27,30,33,52,62,63,73,74,95,],[29,29,29,29,61,65,77,78,79,29,29,29,]),'logic_expression':([20,21,23,27,33,73,74,95,],[31,31,31,31,64,31,31,31,]),'term':([20,21,23,27,30,33,52,62,63,66,67,68,73,74,95,],[32,32,32,32,32,32,32,32,32,80,81,82,32,32,32,]),'factor':([20,21,23,27,30,33,52,62,63,66,67,68,73,74,95,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'lit_value':([20,21,23,27,30,33,52,62,63,66,67,68,73,74,95,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'type':([25,26,],[45,49,]),'logical_op':([29,65,],[52,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement program','program',2,'p_program','lexer.py',142),
  ('program -> statement','program',1,'p_program','lexer.py',143),
  ('statement -> var_declaration','statement',1,'p_statement','lexer.py',152),
  ('statement -> const_declaration','statement',1,'p_statement','lexer.py',153),
  ('statement -> if_statement','statement',1,'p_statement','lexer.py',154),
  ('statement -> while_statement','statement',1,'p_statement','lexer.py',155),
  ('statement -> input_statement','statement',1,'p_statement','lexer.py',156),
  ('statement -> output_statement','statement',1,'p_statement','lexer.py',157),
  ('statement -> function_statement','statement',1,'p_statement','lexer.py',158),
  ('var_declaration -> LET ID OP_TYPE_ASSIGN type OP_VALUE_ASSIGN expression SEMI_COLON','var_declaration',7,'p_var_declaration','lexer.py',165),
  ('const_declaration -> CONST ID OP_TYPE_ASSIGN type OP_VALUE_ASSIGN expression SEMI_COLON','const_declaration',7,'p_const_declaration','lexer.py',171),
  ('if_statement -> IF LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT','if_statement',7,'p_if_statement','lexer.py',177),
  ('if_statement -> IF LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT ELSE CURLYLEFT program CURLYRIGHT','if_statement',11,'p_if_statement','lexer.py',178),
  ('while_statement -> WHILE LPAREN expression RPAREN CURLYLEFT program CURLYRIGHT','while_statement',7,'p_while_statement','lexer.py',187),
  ('input_statement -> READ LPAREN RPAREN SEMI_COLON','input_statement',4,'p_input_statement','lexer.py',193),
  ('output_statement -> PRINT LPAREN expression RPAREN SEMI_COLON','output_statement',5,'p_output_statement','lexer.py',199),
  ('function_statement -> FUNCTION ID LPAREN RPAREN CURLYLEFT statement RETURN expression SEMI_COLON CURLYRIGHT','function_statement',10,'p_function_statement','lexer.py',205),
  ('type -> NUMBER','type',1,'p_type','lexer.py',210),
  ('type -> BOOL','type',1,'p_type','lexer.py',211),
  ('type -> STRING','type',1,'p_type','lexer.py',212),
  ('expression -> simple_expression','expression',1,'p_expression','lexer.py',218),
  ('expression -> OP_MINUS simple_expression','expression',2,'p_expression','lexer.py',219),
  ('expression -> logic_expression','expression',1,'p_expression','lexer.py',220),
  ('simple_expression -> term OP_PLUS simple_expression','simple_expression',3,'p_simple_expression','lexer.py',229),
  ('simple_expression -> term OP_MINUS simple_expression','simple_expression',3,'p_simple_expression','lexer.py',230),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression','lexer.py',231),
  ('logic_expression -> simple_expression logical_op simple_expression','logic_expression',3,'p_logic_expression','lexer.py',240),
  ('logic_expression -> OP_NOT logic_expression','logic_expression',2,'p_logic_expression','lexer.py',241),
  ('term -> factor OP_MULT term','term',3,'p_term','lexer.py',250),
  ('term -> factor OP_DIVIDE term','term',3,'p_term','lexer.py',251),
  ('term -> factor OP_MOD term','term',3,'p_term','lexer.py',252),
  ('term -> factor','term',1,'p_term','lexer.py',253),
  ('factor -> lit_value','factor',1,'p_factor','lexer.py',262),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','lexer.py',263),
  ('factor -> ID','factor',1,'p_factor','lexer.py',264),
  ('logical_op -> OP_AND','logical_op',1,'p_logical_op','lexer.py',275),
  ('logical_op -> OP_OR','logical_op',1,'p_logical_op','lexer.py',276),
  ('logical_op -> OP_MORE_OR_EQUAL','logical_op',1,'p_logical_op','lexer.py',277),
  ('logical_op -> OP_LESS_OR_EQUAL','logical_op',1,'p_logical_op','lexer.py',278),
  ('logical_op -> OP_MORE_THAN','logical_op',1,'p_logical_op','lexer.py',279),
  ('logical_op -> OP_LESS_THAN','logical_op',1,'p_logical_op','lexer.py',280),
  ('logical_op -> OP_NOT_EQUALS','logical_op',1,'p_logical_op','lexer.py',281),
  ('logical_op -> OP_EQUALS','logical_op',1,'p_logical_op','lexer.py',282),
  ('lit_value -> TRUE','lit_value',1,'p_lit_value','lexer.py',288),
  ('lit_value -> FALSE','lit_value',1,'p_lit_value','lexer.py',289),
  ('lit_value -> LIT_NUMBER','lit_value',1,'p_lit_value','lexer.py',290),
  ('lit_value -> LIT_STRING','lit_value',1,'p_lit_value','lexer.py',291),
]
