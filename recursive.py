#################################################################
# FILE : recursive.py
# WRITER : israel_nankencki , israelnan , 305702334
# EXERCISE : intro2cs2 ex7 2022
# DESCRIPTION: several recursion functions .
# STUDENTS I DISCUSSED THE EXERCISE WITH: itamar ami, yotam katz.
# WEB PAGES I USED: none
# NOTES:
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
import recursive_helper
from typing import List, Any


def mult(x: float, y: int) -> float:
    """
    this function is a recursive multiplying in linear complexity with no use of any math operators.
    :param x: a float number to be multiplied.
    :param y: an integer number to multiply x.
    :return: the multiplication of x in y in linear complexity.
    """
    if y == 0:
        return 0
    else:
        return recursive_helper.add(x, mult(x, recursive_helper.subtract_1(y)))


def is_even(n: int) -> bool:
    """
    this is a recursive function for checking whether an integer is even or odd.
    :param n: an integer to check if it even.
    :return: True if n is even, False if n is odd.
    """
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(recursive_helper.subtract_1(recursive_helper.subtract_1(n)))


def log_mult(x: float, y: int) -> float:
    """
    a recursive function to multiply in log complexity.
    :param x: a float number to be multiplied.
    :param y: an integer number to multiply x.
    :return: the multiplication of x in y in log complexity.
    """
    if y == 0:
        return 0
    z = log_mult(recursive_helper.add(x, x), recursive_helper.divide_by_2(y))
    if recursive_helper.is_odd(y):
        return recursive_helper.add(x, z)
    else:
        return z


def power_helper(b: int, n: int) -> int:
    """
    helper function to raise any base in power
    :param b: an integer to be raised in power.
    :param n: the exponential value for b.
    :return: b in power of n.
    """
    if n == 0:
        return 1
    y = power_helper(b, recursive_helper.divide_by_2(n))
    if recursive_helper.is_odd(n):
        return int(log_mult(b, int(log_mult(y, y))))
    else:
        return int(log_mult(y, y))


def is_power_helper(b: int, x: int, n: int) -> bool:
    """
    a recursive helper function to check whether a number is a power base of other number.
    :param b: an integer to be raised in power.
    :param x: an integer to check whether is equal to b in power of n.
    :param n: the possible exponential value for b.
    :return: True if x equal to b in power of any n, False else.
    """
    y = power_helper(b, n)
    if y < x:
        return is_power_helper(b, x, int(recursive_helper.add(n, 1)))
    elif y > x:
        return False
    elif y == x:
        return True
    return False


def is_power(b: int, x: int) -> bool:
    """
    this function is checking whether a number is a base power for other number.
    :param b: an integer to check whether is a power base of x.
    :param x: an integer to check whether is equal to b in power of any integer.
    :return: True if b is a power base of x.
    """
    return is_power_helper(b, x, 0)


def reverse(s: str) -> str:
    """
    a recursive function to reverse a string.
    :param s: string to be reversed.
    :return: the reversed string of s.
    """
    if len(s) == 0:
        return s
    else:
        return recursive_helper.append_to_end(reverse(s[1:]), s[0])


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
    a recursive function to solve the towers of hanoi game.
    :param hanoi: complex object that is a graphic game.
    :param n: integer for the number of disks which the game should move.
    :param src: complex object represent the stick to move disks from.
    :param dst: complex object represent the stick to move disks to.
    :param temp: complex object represent the third stick in the game.
    :return: None.
    """
    if n <= 0:
        return None
    else:
        play_hanoi(hanoi, recursive_helper.subtract_1(n), src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, recursive_helper.subtract_1(n), temp, dst, src)
    return None


def number_of_ones(n: int) -> int:
    """
    a recursive function to count all one digits in range from 1 to n.
    :param n: an integer that is the max value of ones counting.
    :return: the number of ones from 1 to n.
    """
    ones_counter = 0
    if n == 0:
        return 0
    else:
        if n % 10 == 1:
            ones_counter += 1
        if n // 10 == 1:
            ones_counter += 1
        return int(recursive_helper.add(ones_counter, number_of_ones(n - 1)))


def compare_len_helper(l1: List[List[int]], l2: List[List[int]], n: int) -> bool:
    """
    a recursive helper function to check the equality of inner lists length.
    :param l1: first 2d list to be compared.
    :param l2: second 2d list to be compared.
    :param n: an integer to limit the length of the checking process.
    :return: True if the length of both inner lists is identical, False else.
    """
    if len(l1) != len(l2):
        return False
    elif len(l1[n]) != len(l2[n]):
        return False
    else:
        if n < len(l1) - 1:
            return compare_len_helper(l1, l2, int(recursive_helper.add(n, 1)))
        return True


def compare_ints_helper(l1: List[List[int]], l2: List[List[int]], n: int, k: int) -> bool:
    """
    a recursive helper function to check the equality of all ints inside two 2d lists.
    :param l1: first 2d list to be compared.
    :param l2: second 2d list to be compared.
    :param n: an integer to limit the length of the checking process.
    :param k: an index fo integers inside the inner lists.
    :return: True if all integers are equal, False else.
    """
    if len(l1[n]) != 0:
        if l1[n][k] != l2[n][k]:
            return False
        else:
            if k < recursive_helper.subtract_1(len(l1[n])):
                return compare_ints_helper(l1, l2, n, int(recursive_helper.add(k, 1)))
            elif n < recursive_helper.subtract_1(len(l1)):
                return compare_ints_helper(l1, l2, int(recursive_helper.add(n, 1)), 0)
    return True


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """
    this function checks whether two 2d list are completely identical.
    :param l1: first 2d list to be compared.
    :param l2: second 2d list to be compared.
    :return: True if both lists are completely identical, False else.
    """
    if not compare_len_helper(l1, l2, 0):
        return False
    else:
        return compare_ints_helper(l1, l2, 0, 0)


def magic_list_helper(n: int, m: int, magic_lst: List[Any]) -> List[Any]:
    """
    a recursive helper function to build an magic list which any cell is the list of all its previous.
    :param n: integer fo magic list length.
    :param m: integer that counts from 0 to n.
    :param magic_lst: start & partial magic list.
    :return: final magic list with length of n.
    """
    if n < m:
        magic_lst.append(magic_list_helper(n, n, magic_lst))
        return magic_list_helper(int(recursive_helper.add(n, 1)), m, magic_lst)
    else:
        return my_deep_copy(magic_lst)


def my_deep_copy(lst: List[Any]) -> List[Any]:
    return list(eval(repr(lst)))


def magic_list(n: int) -> List[Any]:
    """
    this function returns magic list in the length of n.
    :param n: integer fo magic list length.
    :return: magic list with length of n.
    """
    return magic_list_helper(0, n, [])
