"""
Example:
Violation of DIP
How does it violate the DIP?
The project class is a high-level module and backend & frontend are the low-level modules. In this example,
we found that the high-level module depends on the low-level module. Hence this example are violated the Dependency
Inversion Principle. Let’s solve the problem according to the definition of DIP.
"""


# Example 1:
class BackendDeveloper:
    """This is a low-level module"""

    @staticmethod
    def python():
        print("Writing Python code")


class FrontendDeveloper:
    """This is a low-level module"""

    @staticmethod
    def javascript():
        print("Writing JavaScript code")


class Project:
    """This is a high-level module"""

    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self):
        self.backend.python()
        self.frontend.javascript()
        return "Develop codebase"


project = Project()
print(project.develop())


# Example 2:
class NewsPerson:
    """This is a high-level module"""

    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(NewsPaper().publish(news=news))


class NewsPaper:
    """This is a low-level module"""

    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(f"{news} Hello newspaper")


person = NewsPerson()
print(person.publish("News Paper"))
