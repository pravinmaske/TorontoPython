#import tkinter
#from tkinter.filedialog import askopenfile


#words_file_path=tkinter.filedialog.askopenfilename()
#words_file=open(words_file_path,'r')

#board_file_path=tkinter.filedialog.askopenfilename()
#board_file=open(board_file_path,'r')

#words_file.close()


#print(board)    
"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    if word in wordlist:
        return True
    else:    
        return False


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    string_from_row=''
    i=0
    while(i < len(board[row_index])):
        string_from_row+=board[row_index][i]
        i+=1
    return string_from_row    

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    str_from_column=''
    i=0
    while(i < len(board)):
        str_from_column+=board[i][column_index]
        i+=1
    return str_from_column    
    


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """

    for column_index in range(len(board[0])):
        if word in make_str_from_column(board,column_index):
            return True
    return False    


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """

    return (board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word))
    

def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """

    if (len(word) < 3):
        return 0
    elif (len(word)>=3 and len(word)<=6):
        return len(word)
    elif (len(word)>=7 and len(word)<=9):
        return (len(word)*2)
    elif (len(word)>10):
        return (len(word)*3)
        


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    #if word in board_contains_word(board, word):
    player_info[1]=player_info[1]+word_score(word)
    print(player_info)
            
    
def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    count=0
    for word in words:
        if (board_contains_word(board, word)):
            count+=1
    return count        

    


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    #words_file_path=tkinter.filedialog.askopenfilename()
    #words_file=open(words_file_path,'r')

    words_list=[]

    words=words_file.readlines()

    for word in words:
        word=word.rstrip('\n')
        words_list.append(word)
    print(words_list)
    #return words_list


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """

    board_row=[]
    board=[]
    i=0
    for line in board_file:
        line=line.rstrip('\n')
        board_row+=line
        board.insert(i,board_row)
        i+=1
        board_row=[]  
    return board
