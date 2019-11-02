"""
Solution:
"""


# Example 1:


class BackendDeveloper:
    """This is a low-level module"""

    def develop(self):
        self.__python_code()

    @staticmethod
    def __python_code():
        print("Writing Python code")


class FrontendDeveloper:
    """This is a low-level module"""

    def develop(self):
        self.__javascript()

    @staticmethod
    def __javascript():
        print("Writing JavaScript code")


class Developers:
    """An Abstract module"""

    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self):
        self.backend.develop()
        self.frontend.develop()


class Project:
    """This is a high-level module"""

    def __init__(self):
        self.__developers = Developers()

    def develops(self):
        return self.__developers.develop()


project = Project()
print(project.develops())


# Example 2:


class NewsPerson:
    """This is a high-level module"""

    @staticmethod
    def publish(news: str, publisher=None) -> None:
        print(publisher.publish(news=news))


class NewsPaper:
    """This is a low-level module"""

    @staticmethod
    def publish(news: str) -> None:
        print("{} news paper".format(news))


class Facebook:
    """This is a low-level module"""

    @staticmethod
    def publish(news: str) -> None:
        print(f"{news} - share this post on {news}")


person = NewsPerson()
person.publish("hello", NewsPaper())
person.publish("facebook", Facebook())
