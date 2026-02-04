from . import executor

def compile(source_name, executable_name):
    executor.execute(f"!nvcc src/{source_name} -o {executable_name}")