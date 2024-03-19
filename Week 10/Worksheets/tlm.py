"""CSC108 Tiny Language Model"""

from typing import TextIO
import random

def generate_random_data(training_file: ...                 ,
                         context_length: ...                ,
                         num_words: ...         ) -> ...        :
    """Return randomly generated data with num_words words based on a context
    of context_length words from the training text in open file training_file.
    """
