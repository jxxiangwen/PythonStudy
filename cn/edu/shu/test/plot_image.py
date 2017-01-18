import matplotlib.pyplot as plt


def topic_num():
    #     print(linesList1)
    linesList1 = [(20, 85), (40, 85), (60, 85), (80, 85), (100, 85), (120, 85), (140, 85),
                  (160, 85), (180, 85), (200, 85)]
    linesList2 = [(20, 42), (40, 59), (60, 70), (80, 79), (100, 85), (120, 90), (140, 92.0),
                  (160, 88), (180, 80), (200, 71)]
    linesList3 = [(20, 46), (40, 61), (60, 72), (80, 81), (100, 84), (120, 91.5), (140, 91.8),
                  (160, 87), (180, 75), (200, 68)]
    linesList4 = [(20, 91.6), (40, 91.6), (60, 91.6), (80, 91.6), (100, 91.6), (120, 91.6), (140, 91.6),
                  (160, 91.6), (180, 91.6), (200, 91.6)]
    print(linesList1)
    #     years1 = [string.atof(x[0]) for x in linesList1]
    years1 = [x[0] for x in linesList1]
    price1 = [x[1] for x in linesList1]
    years2 = [x[0] for x in linesList2]
    price2 = [x[1] for x in linesList2]
    years3 = [x[0] for x in linesList3]
    price3 = [x[1] for x in linesList3]
    years4 = [x[0] for x in linesList4]
    price4 = [x[1] for x in linesList4]
    plt.plot(years1, price1, 'b+', label='Cosine Similarity', color='black')
    plt.plot(years1, price1, ':', color='black')
    plt.plot(years2, price2, 'b^', label='Segment with dynamic constant method', color='black')
    plt.plot(years2, price2, ':', color='black')
    plt.plot(years3, price3, 'b.', label='Segment with threshold method', color='black')
    plt.plot(years3, price3, '--', color='black')
    plt.plot(years4, price4, 'bx', label='Neural Networks', color='black')
    plt.plot(years4, price4, '-.', color='black')
    plt.xlabel('Number of Topics')
    plt.ylabel('Degree of Accuracy')
    plt.ylim(40, 140)
    plt.title('Results')
    plt.legend()
    plt.show()


def threshold():
    #     print(linesList1)
    linesList1 = [(0.1, 85), (0.2, 85), (0.3, 85), (0.4, 85), (0.5, 85), (0.6, 85), (0.7, 85),
                  (0.8, 85), (0.9, 85), (1, 85)]
    linesList2 = [(0.1, 92.0), (0.2, 92.0), (0.3, 92.0), (0.4, 92.0), (0.5, 92.0), (0.6, 92.0), (0.7, 92.0),
                  (0.8, 92.0), (0.9, 92.0), (1, 92.0)]
    linesList3 = [(0.1, 10.0), (0.2, 40.0), (0.3, 75.5), (0.4, 88.0), (0.5, 90.5), (0.6, 92.5), (0.7, 93.5),
                  (0.8, 96.4), (0.9, 98.0), (1, 99)]
    linesList4 = [(0.1, 91.6), (0.2, 91.6), (0.3, 91.6), (0.4, 91.6), (0.5, 91.6), (0.6, 91.6), (0.7, 91.6),
                  (0.8, 91.6), (0.9, 91.6), (1, 91.6)]

    #     years1 = [string.atof(x[0]) for x in linesList1]
    years1 = [x[0] for x in linesList1]
    price1 = [x[1] for x in linesList1]
    years2 = [x[0] for x in linesList2]
    price2 = [x[1] for x in linesList2]
    years3 = [x[0] for x in linesList3]
    price3 = [x[1] for x in linesList3]
    years4 = [x[0] for x in linesList4]
    price4 = [x[1] for x in linesList4]
    plt.plot(years1, price1, 'b+', label='Cosine Similarity', color='black')
    plt.plot(years1, price1, '-', color='black')
    plt.plot(years2, price2, 'b^', label='Segment with dynamic constant method', color='black')
    plt.plot(years2, price2, ':', color='black')
    plt.plot(years3, price3, 'b.', label='Segment with threshold method', color='black')
    plt.plot(years3, price3, '--', color='black')
    plt.plot(years4, price4, 'bx', label='Neural Networks', color='black')
    plt.plot(years4, price4, '-.', color='black')
    plt.xlabel('Threshold of threshold method')
    plt.ylabel('Degree of Accuracy')
    plt.ylim(0, 140)
    plt.title('Results')
    plt.legend()
    plt.show()


def degree():
    linesList1 = [(0.1, 10), (0.2, 26), (0.3, 50), (0.4, 65), (0.5, 85), (0.6, 90), (0.7, 93.5),
                  (0.8, 95.5), (0.9, 97), (1, 99)]
    linesList2 = [(0.1, 12), (0.2, 30), (0.3, 57), (0.4, 73), (0.5, 90.0), (0.6, 93.5), (0.7, 93.7),
                  (0.8, 97.9), (0.9, 98.0), (1, 99)]
    linesList3 = [(0.1, 8), (0.2, 30), (0.3, 60), (0.4, 79), (0.5, 92.5), (0.6, 93.8), (0.7, 94.2),
                  (0.8, 97.5), (0.9, 98.0), (1, 99)]
    linesList4 = [(0.1, 20), (0.2, 42), (0.3, 69), (0.4, 84), (0.5, 91.6), (0.6, 95), (0.7, 97),
                  (0.8, 98), (0.9, 98.9), (1, 99)]


    print(linesList1)
    #     years1 = [string.atof(x[0]) for x in linesList1]
    years1 = [x[0] for x in linesList1]
    price1 = [x[1] for x in linesList1]
    years2 = [x[0] for x in linesList2]
    price2 = [x[1] for x in linesList2]
    years3 = [x[0] for x in linesList3]
    price3 = [x[1] for x in linesList3]
    years4 = [x[0] for x in linesList4]
    price4 = [x[1] for x in linesList4]
    plt.plot(years1, price1, 'b+', label='Cosine Similarity', color='black')
    plt.plot(years1, price1, ':', color='black')
    plt.plot(years2, price2, 'b^', label='Segment with dynamic constant method', color='black')
    plt.plot(years2, price2, ':', color='black')
    plt.plot(years3, price3, 'b.', label='Segment with threshold method', color='black')
    plt.plot(years3, price3, '--', color='black')
    plt.plot(years4, price4, 'bx', label='Neural Networks', color='black')
    plt.plot(years4, price4, '-.', color='black')
    plt.xlabel('Matching threshold')
    plt.ylabel('Degree of Accuracy')
    plt.ylim(0, 140)
    plt.title('Results')
    plt.legend()
    plt.show()


def topic_num_recall():
    #     print(linesList1)
    linesList1 = [(20, 85.9), (40, 85.9), (60, 85.9), (80, 85.9), (100, 85.9), (120, 85.9), (140, 85.9),
                  (160, 85.9), (180, 85.9), (200, 85.9)]
    linesList2 = [(20, 49), (40, 67), (60, 79), (80, 85), (100, 89), (120, 92), (140, 94.8),
                  (160, 91), (180, 86), (200, 77)]
    linesList3 = [(20, 51), (40, 70), (60, 79), (80, 86), (100, 88), (120, 91.6), (140, 94.5),
                  (160, 92), (180, 87), (200, 80)]
    linesList4 = [(20, 93.6), (40, 93.6), (60, 93.6), (80, 93.6), (100, 93.6), (120, 93.6), (140, 93.6),
                  (160, 93.6), (180, 93.6), (200, 93.6)]

    print(linesList1)
    #     years1 = [string.atof(x[0]) for x in linesList1]
    years1 = [x[0] for x in linesList1]
    price1 = [x[1] for x in linesList1]
    years2 = [x[0] for x in linesList2]
    price2 = [x[1] for x in linesList2]
    years3 = [x[0] for x in linesList3]
    price3 = [x[1] for x in linesList3]
    years4 = [x[0] for x in linesList4]
    price4 = [x[1] for x in linesList4]
    plt.plot(years1, price1, 'b+', label='Cosine Similarity', color='black')
    plt.plot(years1, price1, ':', color='black')
    plt.plot(years2, price2, 'b^', label='Segment with dynamic constant method', color='black')
    plt.plot(years2, price2, ':', color='black')
    plt.plot(years3, price3, 'b.', label='Segment with threshold method', color='black')
    plt.plot(years3, price3, '--', color='black')
    plt.plot(years4, price4, 'bx', label='Neural Networks', color='black')
    plt.plot(years4, price4, '-.', color='black')
    plt.xlabel('Number of Topics')
    plt.ylabel('F1 Value')
    plt.ylim(40, 130)
    plt.title('Results')
    plt.legend()
    plt.show()


def threshold_recall():
    #     print(linesList1)
    linesList1 = [(0.1, 85.9), (0.2, 85.9), (0.3, 85.9), (0.4, 85.9), (0.5, 85.9), (0.6, 85.9), (0.7, 85.9),
                  (0.8, 85.9), (0.9, 85.9), (1, 85.9)]
    linesList2 = [(0.1, 90.5), (0.2, 90.5), (0.3, 90.5), (0.4, 90.5), (0.5, 90.5), (0.6, 90.5), (0.7, 90.5),
                  (0.8, 90.5), (0.9, 90.5), (1, 90.5)]
    linesList3 = [(0.1, 20.1), (0.2, 46.1), (0.3, 80.1), (0.4, 89.6), (0.5, 92.6), (0.6, 94), (0.7, 87),
                  (0.8, 79), (0.9, 64), (1, 51)]
    linesList4 = [(0.1, 93.6), (0.2, 93.6), (0.3, 93.6), (0.4, 93.6), (0.5, 93.6), (0.6, 93.6), (0.7, 93.6),
                  (0.8, 93.6), (0.9, 93.6), (1, 93.6)]

    print(linesList1)
    #     years1 = [string.atof(x[0]) for x in linesList1]
    years1 = [x[0] for x in linesList1]
    price1 = [x[1] for x in linesList1]
    years2 = [x[0] for x in linesList2]
    price2 = [x[1] for x in linesList2]
    years3 = [x[0] for x in linesList3]
    price3 = [x[1] for x in linesList3]
    years4 = [x[0] for x in linesList4]
    price4 = [x[1] for x in linesList4]
    plt.plot(years1, price1, 'b+', label='Cosine Similarity', color='black')
    plt.plot(years1, price1, ':', color='black')
    plt.plot(years2, price2, 'b^', label='Segment with dynamic constant method', color='black')
    plt.plot(years2, price2, ':', color='black')
    plt.plot(years3, price3, 'b.', label='Segment with threshold method', color='black')
    plt.plot(years3, price3, '--', color='black')
    plt.plot(years4, price4, 'bx', label='Neural Networks', color='black')
    plt.plot(years4, price4, '-.', color='black')
    plt.xlabel('Threshold of threshold method')
    plt.ylabel('F1 Value')
    plt.ylim(0, 140)
    plt.title('Results')
    plt.legend()
    plt.show()


def degree_recall():
    linesList1 = [(0.1, 16), (0.2, 36), (0.3, 57), (0.4, 73), (0.5, 82), (0.6, 85.9), (0.7, 82),
                  (0.8, 73), (0.9, 62), (1, 50.5)]
    linesList2 = [(0.1, 14), (0.2, 40), (0.3, 62), (0.4, 79), (0.5, 85), (0.6, 90.5), (0.7, 81),
                  (0.8, 70), (0.9, 54), (1, 51)]
    linesList3 = [(0.1, 17), (0.2, 37), (0.3, 67), (0.4, 75), (0.5, 89), (0.6, 94), (0.7, 84),
                  (0.8, 70), (0.9, 53), (1, 50.6)]
    linesList4 = [(0.1, 12), (0.2, 37), (0.3, 71), (0.4, 84), (0.5, 93.6), (0.6, 90.5), (0.7, 80),
                  (0.8, 71), (0.9, 54), (1, 50.3)]

    print(linesList1)
    #     years1 = [string.atof(x[0]) for x in linesList1]
    years1 = [x[0] for x in linesList1]
    price1 = [x[1] for x in linesList1]
    years2 = [x[0] for x in linesList2]
    price2 = [x[1] for x in linesList2]
    years3 = [x[0] for x in linesList3]
    price3 = [x[1] for x in linesList3]
    years4 = [x[0] for x in linesList4]
    price4 = [x[1] for x in linesList4]
    plt.plot(years1, price1, 'b+', label='Cosine Similarity', color='black')
    plt.plot(years1, price1, ':', color='black')
    plt.plot(years2, price2, 'b^', label='Segment with dynamic constant method', color='black')
    plt.plot(years2, price2, ':', color='black')
    plt.plot(years3, price3, 'b.', label='Segment with threshold method', color='black')
    plt.plot(years3, price3, '--', color='black')
    plt.plot(years4, price4, 'bx', label='Neural Networks', color='black')
    plt.plot(years4, price4, '-.', color='black')
    plt.xlabel('Matching threshold')
    plt.ylabel('F1 Value')
    plt.ylim(0, 140)
    plt.title('Results')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    topic_num()
    threshold()
    degree()
    topic_num_recall()
    threshold_recall()
    degree_recall()
