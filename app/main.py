import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    if command == 'echo':
        print(args[0])
    elif command == 'echo_stderr':
        print(args[0], file=sys.stderr)

    # completed_process = subprocess.run([command, *args], capture_output=True)
    # print(completed_process.stdout.decode("utf-8"))


if __name__ == "__main__":
    main()
