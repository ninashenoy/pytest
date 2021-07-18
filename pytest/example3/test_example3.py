import pytest

###########################################
class Test_Student():
    def setup(self):
        print("\ncalling setup")
        self.name = "Nina"
        self.age = 21
        return

    def test_name(self):
        assert self.name=="Nina"
        return

    def test_age(self):
        assert self.age==21
        return

    

