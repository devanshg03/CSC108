from typing import TextIO

def is_correct(file: TextIO, word: str) -> bool:
    """Return True if and only if word is in file.
    
    >>> words_file = open('dictionary.txt')
    >>> is_correct(words_file, 'Zyrtec')
    True
    >>> words_file.close()
    >>> words_file = open('dictionary.txt')
    >>> is_correct(words_file, 'lolz')
    False
    >>> words_file.close()
    """
    return any(word == line.strip() for line in file)




def write_ascii_triangle(outfile: TextIO, block: str, sidelength: int) -> None:
    """Write an ascii isosceles right triangle using block that is sidelength
    characters wide and high to outfile. The right angle should be in the
    upper-left corner. 

    Precondition: len(block) == 1

    For example, given block="@" and sidelength=4, the
    following should be written to the file:
    
    @@@@
    @@@
    @@
    @
    """
    for i in range(sidelength, 0, -1):
        outfile.write(block * i + '\n')
    outfile.close()
