import subprocess
import sys
import os
from datetime import datetime

def get_log_path():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    return os.path.join("logs", f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

def main():
    log_path = get_log_path()
    print("Запуск автотестов...")
    print(f"Лог: {log_path}")
    print(f"Команда: {sys.executable} -m pytest -s -v")

    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            "-s", "-v"
        ])
        return_code = result.returncode
    except KeyboardInterrupt:
        print("\nЗапуск прерван.")
        return_code = 1

    print(f"Лог сохранён: {log_path}")
    print(f"Статус: {'SUCCESS' if return_code == 0 else 'FAILED'}")
    sys.exit(return_code)

if __name__ == "__main__":
    main()