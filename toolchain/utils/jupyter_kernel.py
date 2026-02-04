from IPython import get_ipython
from dataclasses import dataclass, field
from typing import Any

@dataclass
class CellExecutor:
    ipython: Any = field(default_factory=get_ipython)
    
    def execute(self, code: str):
        result = self.ipython.run_cell(code)
        if result.error_in_exec:
            raise RuntimeError(result.error_in_exec)
        return result