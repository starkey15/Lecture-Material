"""
class varible - variable that works for all methods of a class
"""

"""
File: student.py
Resources to manage a student's name and test scores.
"""


class Student(object):
    """Represents a student."""

    def __init__(self, name: str, number: float):
        """
        Initialize a Student instance with given name and the number of scores to associate with the given Student.
        :param name: The name of this Student.
        :param number: The number of scores to track for this Student; all scores are initially 0.
        """
        self._name = name
        self._scores = [0] * number

    def get_name(self) -> str:
        """
        Name accessor method.
        :return: The name of this Student is returned.
        """
        return self._name

    def set_score(self, score_index: int, score: float) -> None:
        """
        Score mutator method for the ith score associated with this Student when counting from 1.
        :param score_index: The index of the score to set or change.
        :param score: The new score to keep that is accessible via the given index.
        :return: None
        """
        self._scores[score_index - 1] = score

    def get_score(self, score_index) -> float:
        """
        Score accessor method for the ith score associated with this Student when counting from 1.
        :param score_index: The index of the score to access (when counting from 1).
        :return: The ith score associated with this Student is returned, when counting from 1.
        """
        return self._scores[score_index - 1]

    def get_average(self) -> float:
        """
        Calculate the average score associated with this Student.
        :return: The average score of all the scores for this Student is returned.
        """
        return sum(self._scores) / len(self._scores)

    def get_high_score(self) -> float:
        """
        Determine the highest score associated with this Student.
        :return: The highest score associated with this Student is returned.
        """
        return max(self._scores)

    def __str__(self):
        """
        Return a string representation of this Student.
        :return: A string representation of this Student is returned.
        """
        return "Name: " + self._name + "\nScores: " + \
               " ".join(map(str, self._scores))


def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    student.set_score(1, 89)
    for i in range(2, 6):
        student.set_score(i, 100)
    print(student)
    print("{} has an average score of {}.".format(student.get_name(), student.get_average()))
    print("{}'s highest score is {}.".format(student.get_name(), student.get_high_score()))
    print("{}'s first score was {}.".format(student.get_name(), student.get_score(1)))
    help(Student)


if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------#

"""
File: rational.py
Resources to manipulate rational numbers.
"""


class Rational(object):
    """Represents a rational number."""

    def __init__(self, numerator: int, denominator: int):
        """
        Constructor creates a number with the given numerator and denominator and reduces it to lowest terms.
        :param numerator: the numerator of this Rational number
        :param denominator: the denominator of this Rational number
        """
        self._numerator = numerator
        self._denominator = denominator
        self._reduce()

    def numerator(self) -> int:
        """
        Returns the numerator.
        :return The numerator of this Rational number is returned.
        """
        return self._numerator

    def denominator(self) -> int:
        """
        Returns the denominator.
        :return The denominator of this Rational number is returned.
        """
        return self._denominator

    def __str__(self) -> str:
        """
        Returns the string representation of the number.
        :return A string representation of this Rational number is returned.
        """
        return str(self._numerator) + "/" + str(self._denominator)

    def _reduce(self) -> None:
        """
        Helper to reduce the number to lowest terms. Note that the name with the "_" prefix *suggests* this is a private
        method.
        """
        divisor = self._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // divisor
        self._denominator = self._denominator // divisor

    def _gcd(self, a, b) -> int:
        """
        Euclid's algorithm for greatest common divisor. Note that the name with the "_" prefix *suggests* this is a
        private method.
        :param a: an integer
        :param b: another integer
        :return The greatest common divisor of the parameters a and b is returned.
        """
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    # Methods for arithmetic and comparisons go here

    def __add__(self, other):
        """
        Returns the sum of the numbers.
        :param other: the right-hand operand of of self + other
        :return The sum of this Rational number and the other is returned.
        """
        new_numerator = self._numerator * other.denominator() + other.numerator() * self._denominator
        new_denominator = self._denominator * other.denominator()
        return Rational(new_numerator, new_denominator)

    def __lt__(self, other):
        """
        Returns self < other.
        :param other: The right-hand side of the expression self < other
        :return True is returned if self < other; False otherwise.
        """
        extremes = self._numerator * other.denominator()
        means = other.numerator() * self._denominator
        return extremes < means

    def __ge__(self, other):
        """
        Returns self >= other.
        :param other: The right-hand side of the expression self >= other
        :return True is returned if self >= other; False otherwise.
        """
        extremes = self._numerator * other.denominator()
        means = other.numerator() * self._denominator
        return extremes >= means

    def __eq__(self, other):
        """
        Tests self and other for equality.
        :param other: The right-hand side of the expression self == other
        :return True is returned if self == other; False otherwise.
        """
        if self is other:
            return True
        elif not isinstance(other, Rational):
            return False
        else:
            return self._numerator == other.numerator() and \
                   self._denominator == other.denominator()


def main():
    one_half = Rational(1, 2)
    one_sixth = Rational(1, 6)
    print("one_half =              {}".format(one_half))
    print("one_half + one_sixth =  {}".format(one_half + one_sixth))
    print("one_half == one_sixth = {}".format(one_half == one_sixth))
    print("one_half >= one_sixth = {}".format(one_half >= one_sixth))


if __name__ == "__main__":
    main()