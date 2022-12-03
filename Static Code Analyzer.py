import sys, os, string, ast, re


def check_file(f, p):
    blank = 0
    for i, line in enumerate(f, start=1):
        if len(line) > 79:
            print(f'{p}: Line {i}: S001 Too long')
        if (len(line) - len(line.lstrip(' '))) % 4 != 0:
            print(f'{p}: Line {i}: S002 Indentation is not a multiple of four')
        if '#' in line and line.split('#')[0].strip().endswith(';'):
            print(f'{p}: Line {i}: S003 Unnecessary semicolon')
        if '#' not in line and line.strip().endswith(';'):
            print(f'{p}: Line {i}: S003 Unnecessary semicolon')
        if not line.startswith('#') and '#' in line and not line.split('#')[0].endswith('  '):
            print(f'{p}: Line {i}: S004 At least two spaces before inline comment required')
        if '#' in line and 'todo' in line.split('#')[1].lower():
            print(f'{p}: Line {i}: S005 TODO found')
        if not line.strip():
            blank += 1
        else:
            if blank > 2:
                print(f'{p}: Line {i}: S006 More than two blank lines used before this line')
            blank = 0
        if line.strip().startswith('def  ') or line.startswith('class  '):
            print(f'{p}: Line {i}: S007 Many spaces after construct')
        if line.startswith('class'):
            cls = line.split('class')[1].split('(')[0].split(':')[0].strip()
            if '_' in cls or cls[0] not in string.ascii_uppercase:
                print(f'{p}: Line {i}: S008 Class name not CamelCase')
        if line.strip().startswith('def'):
            func = line.split('def')[1].split('(')[0].strip()
            if any(char in string.ascii_uppercase for char in func):
                print(f'{p}: Line {i}: S009 Function not snake_case')
    file_read = open(p).read()
    tree = ast.parse(file_read)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for argument_name in [a.arg for a in node.args.args]:
                if re.match(r'^[A-Z]', argument_name):
                    print(f'{p}: Line {node.lineno}: S010 Argument name arg_name should be written in snake_cas')
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):
                if re.match(r'^[A-Z]', node.id):
                    print(f'{p}: Line {node.lineno}: S011 Variable var_name should be written in snake_case')
        if isinstance(node, ast.FunctionDef):
            for item in node.args.defaults:
                if isinstance(item, ast.List):
                    print(f'{p}: Line {node.lineno}: S012 The default argument value is mutable')


path = sys.argv[1]
if os.path.isfile(path):
    with open(path,'r') as file:
        check_file(file, path)
elif os.path.isdir(path):
    for file in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
        if file == 'tests.py':
            continue
        path_to_file = os.path.join(path,file)
        with open(path_to_file,'r') as file_to_check:
            check_file(file_to_check, path_to_file)
