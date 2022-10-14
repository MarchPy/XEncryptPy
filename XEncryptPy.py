import Frames.Application as App

NAME_PROGRAM = "Encrypt Files"
VERSION_PROGRAM = "0.1.0"


def main():
    app = App.Application(
            name_program=NAME_PROGRAM,
            version=VERSION_PROGRAM
        )
    app.mainloop()


if __name__ == "__main__":
    main()    
