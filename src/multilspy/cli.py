import sys

def main(message="hello multilspy"):
    """Entry point for the multilspy-init command."""
    print(message)

if __name__ == "__main__":
    # 获取命令行参数
    message = sys.argv[1] if len(sys.argv) > 1 else "hello multilspy"
    main(message) 