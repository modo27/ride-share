from src.main.constants import VALID_COMMANDS_VS_ARGUMENTS
from src.main.ride_share import RideShare


class CommandService:
    def __init__(self, input_file):
        self.__input_file = input_file

    def execute(self):
        ride_share = RideShare()
        with open(self.__input_file) as fp:
            Lines = fp.readlines()
            for line in Lines:
                line = line.strip()
                command_name, arguments = self.get_commands_and_arguments(line)
                if not (command_name and arguments):
                    continue
                ride_share.parse_and_execute_command(command_name, arguments)

    @classmethod
    def get_commands_and_arguments(cls, text):

        arguments = []
        splited_text = text.split(" ")

        command_name = splited_text[0]
        if command_name in VALID_COMMANDS_VS_ARGUMENTS:
            arguments = splited_text[1:]
            if len(arguments) == VALID_COMMANDS_VS_ARGUMENTS[command_name]:
                return command_name, arguments
        return None, None
