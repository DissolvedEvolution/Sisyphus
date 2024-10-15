import os

def generate_tree(startpath, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = ['.git', '__pycache__', 'venv', 'env']
    if exclude_files is None:
        exclude_files = ['.gitignore', '.env']

    tree = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
        
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Add directory name
        tree.append(f'{indent}{os.path.basename(root)}/')
        
        # Add files
        for file in files:
            if file not in exclude_files:
                tree.append(f'{indent}│   {file}')

    return '\n'.join(tree)

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    print(f"Project structure for: {os.path.basename(project_root)}")
    print("=" * 40)
    print(generate_tree(project_root))