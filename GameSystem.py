class GameSystem():

    def __init__(self, failNum = 0, failLimit = 3):
        self.failNum = failNum
        self.failLimit = failLimit

    def check_fail(self):
        if self.failNum >= self.failLimit:
            return True
        return False

    def add_failure(self):
        self.failNum += 1
        print(self.failNum)


