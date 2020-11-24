from binary_search import binary_search


def test_binary_search():
    assert binary_search([1, 2, 3, 4], 3) == 2
    assert binary_search([1, 2, 3, 4], 5) == -1
    assert binary_search([1, 2, 3, 4], 1) == 0
    assert binary_search([1, 2, 3, 4], 3) == 3
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    #assert binary_search([1, 2, 3, 4, 5], 5) == 4
   #assert binary_search([1, 2, 3, 4, 5], 3) == 2