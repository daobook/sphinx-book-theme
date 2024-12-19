import inspect
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[0]
sys.path.extend([str(ROOT/'src')])
if not hasattr(inspect, 'getargspec'): # 修复
    inspect.getargspec = inspect.getfullargspec
    
from tao.tools.write import site

namespace = site('docs', target='docs/build/html')
