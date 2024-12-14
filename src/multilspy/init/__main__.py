"""
Multilspy init command.
Can be run with: python -m multilspy.init "message"
"""
import sys
from ..cli import main

if __name__ == "__main__":
    # 获取命令行参数
    message = sys.argv[1] if len(sys.argv) > 1 else "hello multilspy"
    main(message) 