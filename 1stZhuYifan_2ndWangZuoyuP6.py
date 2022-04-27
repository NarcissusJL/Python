"""
    Purpose: spend more time practicing with lists, 2D lists, and nested for loops.
    Author: Yifan Zhu/ Zuoyu Wang
    Date: 14/ Nov/ 2018
    CS 109, 2018
"""

def board_1():
    """
    purpose: Make our first logical puzzle game board
    paramater: None
    retun value: board_1
    """
    a = [[] for i in range(5)]

    a[0] = ['','byengo_bat','eldar_elk','nibner_newt','osbele_oryx']
    a[1] = ['2006' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[2] = ['2007' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[3] = ['2008' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[4] = ['2009' ,"empty " ,"empty" ,"empty" ,"empty"]

    board_1 = a
    print("===========================================================================")
    for i in range(len(board_1)):
        for j in range(len(board_1[1])):
            print( '{0:<15}'.format(board_1[i][j]), end = "")
        print("|", "\n")

    return board_1


def board_2():
    """
    purpose: Make our second logical puzzle game board
    paramater: None
    return value: board_2
    """
    a = [[] for i in range(5)]

    a[0] = ['','245','385','455','560']
    a[1] = ['2006' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[2] = ['2007' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[3] = ['2008' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[4] = ['2009' ,"empty " ,"empty" ,"empty" ,"empty"]

    board_2 = a
    print("===========================================================================")
    for i in range(len(board_2)):
        for j in range(len(board_2[1])):
            print( '{0:<15}'.format(board_2[i][j]), end = "")
        print("|", "\n")

    return board_2


def board_3():
    """
    purpose: Make our third logical puzzle game board
    paramater: None
    return value: board_3
    """
    a = [[] for i in range(5)]

    a[0] = ['','byengo_bat','eldar_elk','nibner_newt','osbele_oryx']
    a[1] = ['245' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[2] = ['385' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[3] = ['455' ,"empty " ,"empty" ,"empty" ,"empty"]
    a[4] = ['560' ,"empty " ,"empty" ,"empty" ,"empty"]

    board_3 = a
    print("===========================================================================")
    for i in range(len(board_3)):
        for j in range(len(board_3[1])):
            print( '{0:<15}'.format(board_3[i][j]), end = "")
        print("|", "\n")

    return board_3


def update_board(board_1, board_2, board_3):
    """
    purpose: Update our logical puzzle game board
    paramater: board_1, board_2, board_3
    return value: Updated board for the logical puzzle game
    """

    print("1): The species with a population size of 245 was listed 1 year after the byengo bat")
    print("2): The species with a population size of 385 is either the animal added to the list in 2009 or the elder elk")
    print("3): The species added to the list in 2008 has 385 surviving individuals")
    print("4): The nibner newet is either the species added to the list in 2009 or the animal with a population size of 455", "\n")


    while (True):

        clue = input("Please give me a three words clue: ")
        clue = clue.split()
        factor1 = clue[0]
        factor2 = clue[2]
        trueOrF = clue[1]

        for i in range(5):   #(Take the clue from the user while testing for the first board)

            if factor1 in board_1[i]:
                for j in range(5):
                    if factor2 in board_1[j]:

                        row1 = i
                        col1 = board_1[i].index(factor1)
                        row2 = j
                        col2 = board_1[j].index(factor2)

                        if row2 > 0:
                            row = row2
                        else:
                            row = row1
                        if col2 > 0:
                            col = col2
                        else:
                            col = col1

                        if 'not' in clue:
                            board_1[row][col] = "X"
                        else:
                            for a in range(1,5):
                                board_1[row][a] = "X"
                                board_1[a][col] = "X"
                                board_1[row][col] = "O"

        print("===========================================================================")
        for i in range(len(board_1)):
            for j in range(len(board_1[1])):
                print( '{0:<15}'.format(board_1[i][j]), end = "")
            print("|", "\n")


        for i in range(5):   #(Take the clue from the user while testing our second board)

            if factor1 in board_2[i]:
                for j in range(5):
                    if factor2 in board_2[j]:

                        row1 = i
                        col1 = board_2[i].index(factor1)
                        row2 = j
                        col2 = board_2[j].index(factor2)

                        if row2 > 0:
                            row = row2
                        else:
                            row = row1
                        if col2 > 0:
                            col = col2
                        else:
                            col = col1

                        if 'not' in clue:
                            board_2[row][col] = "X"
                        else:
                            for a in range(1,5):
                                board_2[row][a] = "X"
                                board_2[a][col] = "X"
                                board_2[row][col] = "O"
        print("===========================================================================")
        for i in range(len(board_2)):
            for j in range(len(board_2[1])):
                print( '{0:<15}'.format(board_2[i][j]), end = "")
            print("|", "\n")


        for i in range(5):   #(Take the clue from user while testing our third board)

            if factor1 in board_3[i]:
                for j in range(5):
                    if factor2 in board_3[j]:

                        row1 = i
                        col1 = board_3[i].index(factor1)
                        row2 = j
                        col2 = board_3[j].index(factor2)

                        if row2 > 0:
                            row = row2
                        else:
                            row = row1
                        if col2 > 0:
                            col = col2
                        else:
                            col = col1

                        if 'not' in clue:
                            board_3[row][col] = "X"
                        else:
                            for a in range(1,5):
                                board_3[row][a] = "X"
                                board_3[a][col] = "X"
                                board_3[row][col] = "O"
        print("===========================================================================")
        for i in range(len(board_3)):
            for j in range(len(board_3[1])):
                print( '{0:<15}'.format(board_3[i][j]), end = "")
            print("|", "\n")
        print("First board update finished, if you still want to play please do the following: ")
        print("===========================================================================")

def main():
    b1 = board_1()
    b2 = board_2()
    b3 = board_3()
    update_board(b1, b2, b3)

main()
