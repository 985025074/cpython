import ast

def print_ast_tree(node, level=0):
    indent = "  " * level
    node_type = type(node).__name__
    
    # 打印节点类型和关键属性
    if isinstance(node, ast.Name):
        print(f"{indent}{node_type}: {node.id}")
    elif isinstance(node, ast.Constant):
        print(f"{indent}{node_type}: {node.value}")
    else:
        print(f"{indent}{node_type}")
    
    # 递归处理子节点
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    print_ast_tree(item, level + 1)
        elif isinstance(value, ast.AST):
            print_ast_tree(value, level + 1)

# 示例代码
# 示例代码
source_code = """
=>
"""

# 使用 exec 模式解析，这样可以包含更多语法
tree = ast.parse(source_code, mode='exec')
print_ast_tree(tree)