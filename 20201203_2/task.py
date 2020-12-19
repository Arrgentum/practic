import sys

def check_annot(self):
        for attr, obj in self.__annotations__.items():
            if not hasattr(self, attr) or not isinstance(getattr(self, attr), obj):
                return False
        return True

class check(type):
    def __init__(self, *ap, **an):
        super().__init__(*ap, **an)
        self.check_annotations = check_annot

exec(sys.stdin.read())
