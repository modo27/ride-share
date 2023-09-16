from sys import argv

from src.main.service.command_service import CommandService


def main(input_file_name=None):
    if not (input_file_name):
        if len(argv) != 2:
            raise Exception("File path not entered")
        input_file_name = argv[-1]
    command_service = CommandService(input_file_name)
    command_service.execute()


if __name__ == "__main__":
    main()
