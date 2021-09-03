from time import sleep


class Chock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
        elif self._minute == 60:
            self._minute = 0
            self._hour += 1
        elif self._hour == 24:
            self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    chock = Chock(00, 00, 00)
    while True:
        print(chock.show())
        sleep(1)
        chock.run()


if __name__ == '__main__':
    main()
