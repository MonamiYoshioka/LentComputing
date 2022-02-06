# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""

# For Task 1E
def get_N_max_integers(dictionary, N):
  """Find the N rivers with the greatest number of monitoring stations

  Args:
      stations (list): list of MonitoringStation objects
      N (int): max number of station numbers

  Returns:
      list: list of N maximum integers in the dictionary values
  """
  
  # Order list (highest values first)
  dictionary = dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))
  
  # Create a list with the N max integers
  numbers = []
  [numbers.append(value) for key, value in dictionary.items() if value not in numbers]
  numbers = numbers[:N]
  return numbers


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)
