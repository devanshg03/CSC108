# WS 1: Understanding the problem to be solved
# WS 2: Think about how to represent the data in the program
# WS 3: How to get data into the program
# WS 4: Write code to process data and generate results
# WS 5: Reflect on issues in program and data

from typing import TextIO
import random
training_file = open('shakespeare.txt', 'r')

def build_context_to_next_words(words_list: list, context_length: int) -> dict[tuple[str], list[str]]:
    """ Retun a dictionary where the keys are context of adjacent words and the values
    are the possible words that we might find after this context.
    
    >>> result = build_context_to_next_words(['to', 'be', 'or', 'not', 'to','be', 'that'], 2)
    >>> result == {('to', 'be'): ['or', 'that'], ('be', 'or'): ['not'], ('or', 'not'): ['to'], ('not', 'to'): ['be']}
    """
    result = {}
    for i in range(len(words_list) - context_length):
        key = tuple(words_list[i:i + context_length])
        if key not in result:
            result[key] = []
        if i + context_length < len(words_list):
            result[key].append(words_list[i + context_length])
    return result

def generate_story(context_to_next_words: dict[tuple[str], list[str]], num_words: int) -> str:
    """Return a randomly generated story of num_words words based on the context_to_next_words dictionary."""
    story_so_far = ''
    all_contexts = list(context_to_next_words.keys())
    context = random.choice(all_contexts)
    # Choose a random start to the story
    for word in context:
        story_so_far = story_so_far + word

    word_count = len(context)

    # Choose a random next word based on the context of the last words
    while word_count < num_words:
        # randomly choose the next word
        possible_next_words = context_to_next_words[context]
        next_word = random.choice(possible_next_words)

        # add the next word to the story
        story_so_far = story_so_far + ' ' + next_word
        word_count += 1

        # update the context
        context = context[1:] + (next_word,)

        if context not in context_to_next_words:
            context = random.choice(all_contexts)
    
    return story_so_far

def generate_random_data(training_file: TextIO, context_length: int, num_words: int) -> str:
    """Return randomly generated data with num_words words based on a context of
    context_length words from the training text open in file_training_filie."""
    # Read in the file and build the words list.
    words = training_file.read().split()

    # Build the context to next words dictionary.
    context_to_next_words = build_context_to_next_words(words, context_length)
    # Generate the story.
    story = generate_story(context_to_next_words, num_words)

    # Return the generated story.
    return story


if __name__ == "__main__":
    import doctest
    # doctest.testmod()