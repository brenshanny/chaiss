import sys
import os
import time
# from picamera import PiCamera


class ChaissSetup(object):
    def __init__(self, starting_name="pawn"):
        self.dir_path = os.getcwd()
        self.change_piece(starting_name)
        # self.camera = PiCamera()

    def change_piece(self, piece = None):
        if piece:
            self.print_empty()
            print("Piece name set to {}".format(piece))
            self.piece_name = piece
        else:
            self.piece_name = input("Please enter a piece name: ")
        self.photos_taken = 0

    def print_main_menu(self):
        print("----------------------")
        print("Current Piece Name: {}".format(self.piece_name))
        print("----------------------")
        print("Total photos taken: {}".format(self.photos_taken))
        self.print_empty()
        print("Please Select an Option")
        print("1: Take Photo")
        print("2: Change piece name")
        print("3: exit")
        self.print_empty(5)

    def print_empty(self, times = 1):
        for i in range(1, times):
            print()

    def exit(self):
        self.print_empty()
        print("Goodbye")
        sys.exit()

    def take_photo(self):
        file_path = "{}/{}_{}".format(self.dir_path, self.piece_name, self.photos_taken)
        print("Saving file to: {}".format(file_path))
        # self.camera.capture(file_path)
        self.photos_taken += 1

    def method_hash(self):
        return {
                "1": self.take_photo,
                "2": self.change_piece,
                "3": self.exit,
                }

    def parse_input(self, entry):
        if int(entry) not in [1, 2, 3]:
            self.parse_input(input("Please enter a number 1, 2, or 3"))
        else:
            self.method_hash()[entry]()

    def run(self):
        while True:
            try:
                self.print_main_menu()
                self.parse_input(input("Your selection: "))
            except KeyboardInterrupt:
                self.print_empty()
                self.exit()


if __name__ == "__main__":
    ChaissSetup("Pawn").run()
