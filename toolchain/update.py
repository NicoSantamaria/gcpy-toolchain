from . import executor

def update(branch_name):
    executor.execute(f"!git fetch origin {branch_name}")
    executor.execute(f"!git pull origin {branch_name}")