# Lab 18 Peaks and Valleys
data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data: list) -> list:
    peaks = []
    for index in range(1, (len(data) - 1)):
        if data[index - 1] < data[index] > data[index + 1]:
            peaks.append(index)
    return peaks


def valleys(data: list) -> list:
    valleys = []
    for index in range(1, (len(data) - 1)):
        if data[index - 1] > data[index] < data[index + 1]:
            valleys.append(index)
    return valleys


def peaks_and_valleys(data: list) -> list:
    peaks_and_valleys_indicies = sorted(peaks(data) + valleys(data))

    return peaks_and_valleys_indicies

def draw_mountains(data):
    sorted_data = list(set(sorted(data)))
    #rows = int(sorted_data[-1])

    for index in range(len(data) - 1):
        if sorted_data[index] > data[index]:
            print(' X ')
        else:
            print(' ')

        
        
        


peaks_and_valleys(data_list)

draw_mountains(data_list)
