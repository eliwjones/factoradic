def build_card_map():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['c', 'd', 'h', 's']

    card_map = {}
    i = 0
    for suit in suits:
        for value in values:
            card = "%s%s" % (value, suit)
            card_map[card] = i
            i += 1

    return card_map


def deck_to_number(deck):
    """
      Since we require 128 bit numbers, use 2^128 as our modulus.

      This will collapse all permutations into their respective
      quotient groups.
    """
    card_map = build_card_map()
    permutation = [card_map[card] for card in deck]

    number = permutation_to_number(permutation)

    return number % (2**128)


def number_to_deck(number):
    card_map = build_card_map()
    inverse_card_map = {value: card for card, value in card_map.items()}
    permutation = number_to_permutation(number, len(card_map))

    deck = [inverse_card_map[value] for value in permutation]

    return deck


"""
  The number_to_permutation() and permutation_to_number() functions are just slight rewrites
  of some code found here:

    http://www.math.umbc.edu/~campbell/Computers/Python/probstat.html#ProbStat-Combin-Permutations

"""


def number_to_permutation(number, length):
    """
      Get digits if we view this in base factorial.
    """
    permutation = []
    number = number % poor_mans_factorial(length)

    ordered_permutation = list(range(length))
    for i in range(1, length):
        digit = (number // poor_mans_factorial(length - i))
        number = (number % poor_mans_factorial(length - i))

        permutation.append(ordered_permutation[digit])

        del ordered_permutation[digit]

    return permutation + ordered_permutation


def permutation_to_number(permutation):
    """
      Treat permutation as a list of digits for a base factorial number.
    """
    length = len(permutation)
    base_permutation = list(range(length))
    number = 0
    for i in range(length):
        index = length - i - 1
        digit = base_permutation.index(permutation[i])

        number += digit * poor_mans_factorial(index)

        del base_permutation[digit]

    return number


def poor_mans_factorial(n, mem={0: 1}):
    """
      Use annoying fact that mem argument will persist over multiple calls for our memoization.
    """
    if n in mem:
        return mem[n]

    x = n * poor_mans_factorial(n - 1, mem)
    mem[n] = x

    return x
