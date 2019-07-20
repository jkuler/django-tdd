import os


class HollyHouse:

    shh_list = ['sec']

    def __init__(self, fon_go_la):
        self.se_ke_le = fon_go_la

    def __getattr__(self, attr):
        if attr in self.shh_list:
            return getattr(self.se_ke_le, attr)


def acient_grave(sec):
    _door = os.environ.get(sec)
    return _door
