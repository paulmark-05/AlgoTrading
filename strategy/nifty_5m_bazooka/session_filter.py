from datetime import time


class SessionFilter:

    @staticmethod
    def entry_allowed(dt):

        t = dt.time()

        return (
            time(9, 25)
            <=
            t
            <=
            time(15, 0)
        )

    @staticmethod
    def force_exit(dt):

        t = dt.time()

        return t >= time(15, 10)