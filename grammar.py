GRAMMAR = r"""
start: statement+

statement: var_definition_with_type
         | write
         | expr ";"


var_definition_with_type: NUM_KW CNAME "=" expr ["," type_spec] ";" 
                       | STR_KW CNAME "=" expr ";" 
                       | LIST_KW CNAME "=" list_expr ";"

write: WRITE_KW "(" expr ("," expr)* ")" ";" 

?expr: expr "==" expr    -> comp
     | expr "!=" expr    -> ncomp
     | expr ">" expr     -> mr
     | expr "<" expr     -> ls
     | expr "+" term     -> plus
     | expr "-" term     -> minus
     | term

?term: term "*" factor   -> multiply
     | term "/" factor   -> divide
     | term "//" factor  -> division_integer
     | factor

?factor: "(" expr ")"
       | "-" factor      -> neg
       | "+" factor      -> pos
       | CNAME           -> get_var
       | ESCAPED_STRING  -> string_val
       | NUMBER          -> number

type_spec: "int" -> type_int
         | "float" -> type_float

list_expr: "[" [expr ("," expr)*] "]" -> make_list

// Ключевые слова с приоритетом
NUM_KW.2: "num"
STR_KW.2: "str"
LIST_KW.2: "list"
WRITE_KW.2: "write"

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.CNAME
%import common.WS
%ignore WS
"""
