import subprocess, sys

if __name__ == "__main__":
    subprocess.check_call([sys.executable, "fastloop_trader.py", "--quiet"])
