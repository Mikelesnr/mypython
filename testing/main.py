class Doing_stuff:
    def __init__(self) -> None:
        pass

    def do_stuff(num):
        try:
            return int(num)+5
        except ValueError as err:
            return err
