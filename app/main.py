import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run([command, *args], capture_output=True, )

    if args[0] == 'echo':
        print(completed_process.stdout.decode("utf-8"))
    elif args[0] == 'echo_stderr':
        print(completed_process.stdout.decode("utf-8"), file=sys.stderr)

    quit(completed_process.returncode)


if __name__ == "__main__":
    main()
