# Lab 18 Peaks and Valleys

data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data: list) -> list:
    peaks = []
    for elevation in range(1, (len(data) - 1)):
        if data[elevation - 1] < data[elevation] > data[elevation + 1]:
            peaks.append(data.index(data[elevation]))
    return peaks


def valleys(data: list) -> list:
    valleys = []
    for elevation in range(1, (len(data) - 1)):
        if data[elevation - 1] > data[elevation] < data[elevation + 1]:
            valleys.append(data.index(data[elevation]))
    return valleys


def peaks_and_valleys(data: list) -> list:
    peaks_and_valleys_indicies = sorted(peaks(data) + valleys(data))

    return peaks_and_valleys_indicies


peaks_and_valleys(data_list)
