# Team Number
# Members:-
# Anas Maher
# Ahlam Mostafa
# Hana Abdelhaq
# Nada Gamal
# Menna Ahmed



f = open("code.txt", "r")
l=[]
l3=[]
for line in f:
    l3.append(line)
    l2 = line.strip().split()
    l.extend(l2)

l = list(filter(None, l))
print(l)

#get lexeme+token
tokens={"operator":["+","-"],"assignment_op":["="],
        "keyword":["if","else"], "identifier":[],
        "punctation":[":",",","(",")","[","]",'"',"'"], "str_literals":[],
        'int_literals':[],"comparison-op":["==" , "!=" , "<" , ">" , "=>" ,"=<"],
        'logical-op' : ["and" , "or"]
}
numt=[]

#{x:[0,int,1,[3,6,7]]}
ident={}
for i in l:

       for j in tokens:
           if i in tokens[j]:
               if j not in numt:
                   numt.append(j)
               print(i, j)
               break
       else:
           if i.isdigit():
               if "int_literal" not in numt:
                   numt.append("int_literal")
               print(i,"int_literal")

           elif isinstance(i,str):
               if l.index(i)+1 != len(l) and l[l.index(i)+1]=="=":
                   x=0
                   if x==0 and ("identifier" not in numt):
                       numt.append("identifier")
                       x+=1
                   if i not in ident:
                       if l[l.index(i)+2].isdigit() or l[l.index(i)+2] in ident:
                          ident[i]=[0,"int",0,[]]
                       else:
                          ident[i] = [0, "str", 0, []]
                   print(i,"identifier")


               else:
                   if "str_literal" not in numt:
                       numt.append("str_literal")
                   print(i,'str_literal')


print(f"number of tokens={len(numt)}")


#symbol table

sizes={"int":28,"str":49,}

for k in ident:
    lines=[]
    data=ident[k]
    if k != list(ident.keys())[0]:
        prev_key = list(ident.keys())[list(ident.keys()).index(k) - 1]
        prev_element_data = ident[prev_key]
        data[0]=prev_element_data[0]+sizes[prev_element_data[1]]
    for line in l3:
        if k in line:
            lines.append((l3.index(line))+1)
    data[2],data[3]=lines[0],lines
    ident[k]=data


print("counter | name | memory location | DataType | line declared | lines refernce ")
ra=list(range(len(ident)))
for counter,ele in zip(ra,ident):
    print(counter+1,ele,*ident[ele],sep="\t\t\t")





#get First
grammar = {
    "<program>": ["<stmts>"],
    "<stmts>": ["<stmt>"],
    "<stmt>": ["<assignment>", "<if-stmt>"],
    "<assignment>": ["<var> = <expr>"],
    "<expr>": ["<term> - <term>", "<term> + <term>", "<term>"],
    "<term>": ["<var>", "const"],
    "<var>": ["<identifier>"],
    "<identifier>": ["<letter>", "<letter> <all-list>"],
    "<all-list>": ["<letter>", "<int>", "_"],
    "<letter>": ["<upper-case>", "<lower-case>"],
    "<upper-case>": ["[A-Z]"],
    "<lower-case>": ["[a-z]"],
    "<int>": ["<digit>"],
    "<digit>": ["[0-9]"],
    "<if-stmt>": ["if <logic-expr> : <stmt>", "else : <stmt>"],
    "<logic-expr>": ["<comparison>", "<comparison> <logical-op> <logic-expr>", "not <logic-expr>"],
    "<comparison>": ["<term> <comparison-op> <term>"],
    "<comparison-op>": ["==", "=!", "<", ">", "<=", ">="],
    "<logical-op>": ["and", "or"]
}


first = {}

def is_terminal(obj):
    return obj not in grammar or obj in ["[A-Z]", "[a-z]", "[0-9]", "_"]

def get_first(obj):

    if obj in first:
        return first[obj]
    first[obj] = set()

    for production in grammar.get(obj, []):
        parts = production.split()
        for part in parts:
            if is_terminal(part):
                if part == "[A-Z]":
                    first[obj].update(chr(c) for c in range(ord('A'), ord('Z') + 1))
                elif part == "[a-z]":
                    first[obj].update(chr(c) for c in range(ord('a'), ord('z') + 1))
                elif part == "[0-9]":
                    first[obj].update(chr(c) for c in range(ord('0'), ord('9') + 1))
                elif part == "_":
                    first[obj].add("_")
                else:
                    first[obj].add(part)
                break
            else:
                first[obj].update(get_first(part) - {""})
                if "" not in first[part]:
                    break
    return first[obj]

for non_terminal in grammar:
    get_first(non_terminal)

for non_terminal, first_set in first.items():
    print(f"First({non_terminal}) = {sorted(first_set)}")



#Parse Tree
class ParseTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"({self.value} -> {', '.join(map(str, self.children))})"


def parse_logic_expr(expr):
    expr_parts = expr.split()
    if len(expr_parts) == 3:
        term1, comparison_op, term2 = expr_parts
        logic_expr_node = ParseTreeNode("<logic-expr>")
        comparison_node = ParseTreeNode("<comparison>")
        comparison_node.add_child(ParseTreeNode(term1))
        comparison_node.add_child(ParseTreeNode(comparison_op))
        comparison_node.add_child(ParseTreeNode(term2))
        logic_expr_node.add_child(comparison_node)
        return logic_expr_node

    return None

def parse_assignment(statement):
    var_part, expr_part = statement.split('=')
    var_part = var_part.strip()
    expr_part = expr_part.strip()

    assignment_node = ParseTreeNode("<assignment>")

    var_node = ParseTreeNode("<var>")
    identifier_node = ParseTreeNode("<identifier>")
    identifier_node.add_child(ParseTreeNode(f"'{var_part}'"))
    var_node.add_child(identifier_node)

    expr_node = ParseTreeNode("<expr>")
    term_node = ParseTreeNode("<term>")

    if expr_part.isdigit():
        const_node = ParseTreeNode("<const>")
        const_node.add_child(ParseTreeNode(expr_part))
        term_node.add_child(const_node)
    else:
        term_node.add_child(ParseTreeNode("<var>"))
        term_node.children[0].add_child(ParseTreeNode(f"'{expr_part.strip()}'"))

    expr_node.add_child(term_node)

    assignment_node.add_child(var_node)
    assignment_node.add_child(ParseTreeNode("="))
    assignment_node.add_child(expr_node)

    return assignment_node

def parse_if_statement(statement):

    if_parts = statement.split("else")
    if_part = if_parts[0].strip()
    else_part = if_parts[1].strip() if len(if_parts) > 1 else None


    if_condition_part, stmt_part = if_part.split(":")
    logic_expr_node = parse_logic_expr(if_condition_part.replace("if", "").strip())
    stmt_node = parse_assignment(stmt_part.strip())


    if_node = ParseTreeNode("<if-stmt>")
    if_node.add_child(logic_expr_node)
    if_node.add_child(ParseTreeNode(":"))
    if_node.add_child(stmt_node)

    if else_part:
        else_stmt_node = parse_assignment(else_part.strip())
        else_node = ParseTreeNode("<else-stmt>")
        else_node.add_child(else_stmt_node)
        if_node.add_child(else_node)

    return if_node

#Parse the first line of an "if" statement
#"if z > m : x = 5 else : x = 2"
statement = l3[1]
parse_tree1 = parse_assignment(statement)
statement2 = "if z > m : x = 5 else : x = 2"
parse_tree2 = parse_if_statement(statement2)


print(parse_tree1)
print(parse_tree2)
