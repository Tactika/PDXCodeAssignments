from lab18_peaks_valleys import peaks, valleys, peaks_and_valleys


def test_peaks():
    assert peaks([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,
                  7, 8, 9, 8, 7, 6, 7, 8, 9]) == [6, 14]

def test_valleys():
    assert valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,
                  7, 8, 9, 8, 7, 6, 7, 8, 9]) == [9, 17]

def test_peaks_and_valleys():
    assert peaks_and_valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6,
                              7, 8, 9, 8, 7, 6, 7, 8, 9]) == [6, 9, 14, 17]
