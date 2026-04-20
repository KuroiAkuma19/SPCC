import re

def lexical_analyzer(expr):
    tokens = re.findall(r'[a-zA-Z_]\w*|\d*\.\d+|\d+|[=+\-*/()]', expr)
    sym = {v: i+1 for i, v in enumerate(dict.fromkeys(t for t in tokens if t[0].isalpha()))}
    return tokens, sym

class Node:
    def __init__(self, v, l=None, r=None):
        self.v, self.l, self.r = v, l, r

def parse(tokens):
    it = iter(tokens); cur = next(it, None)
    def eat(): 
        nonlocal cur
        v, cur = cur, next(it, None)
        return v
    
    def factor(): return Node(eat())
    
    def term():
        n = factor()
        while cur == '*': eat(); n = Node('*', n, factor())
        return n
        
    def expr():
        n = term()
        while cur and cur in '+-': 
            op = eat(); n = Node(op, n, term())
        return n

    if len(tokens) > 1 and tokens[1] == '=':
        id_node = Node(eat()); eat() 
        return Node('=', id_node, expr())
    return expr()

def get_tree_lines(n):
    if not n: return [], 0, 0, 0
    label = str(n.v)
    if not n.l and not n.r: return [label], len(label), 1, len(label)//2
    
    l_lines, l_w, l_h, l_c = get_tree_lines(n.l)
    r_lines, r_w, r_h, r_c = get_tree_lines(n.r)
    
    gap = 2
    w = max(l_w + gap + r_w, len(label))
    res_l_c, res_r_c = l_c, l_w + gap + r_c
    c = (res_l_c + res_r_c) // 2
    
    res = [" " * (c - len(label)//2) + label]
    links = [" "] * w
    if n.l: links[res_l_c] = "/"
    if n.r: links[res_r_c] = "\\"
    res.append("".join(links))
    
    for i in range(max(l_h, r_h)):
        l_p = l_lines[i] if i < l_h else " " * l_w
        r_p = r_lines[i] if i < r_h else " " * r_w
        res.append(l_p + " " * gap + r_p)
    return res, w, len(res), c

if __name__ == "__main__":
    text = input("Enter expression: ")
    tokens, sym = lexical_analyzer(text)
    
    print("\n1. Lexical Analysis\nLexeme   | Token")
    for t in tokens:
        print(f"{t:8} | <{('id, '+str(sym[t])) if t[0].isalpha() else t}>")

    print("\n2. Syntax Analysis")
    root = parse(tokens)
    lines, *_ = get_tree_lines(root)
    for line in lines: print(line)

    print("\n3. Semantic Analysis")
    def validate(n):
        if not n: return True
        val = str(n.v)
        if val.replace('.','',1).isdigit() and '.' not in val:
            print(f"SEMANTIC ERROR: '{val}' is not a float!")
            return False
        return validate(n.l) and validate(n.r)
    
    if validate(root): print("Expression is semantically VALID")
