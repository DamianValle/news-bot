import re
import unicodedata

def is_match(text):
    """
    Check if the text contains any words in the dictionary.

    :param text: The input string.
    :type text: String.

    :returns: The text does contain a match.
    :rtype: Boolean.
    """
    dic_file = open('./dic.txt', 'r')
    match = False

    for line in dic_file.readlines():
        translation = line.split('\n')[0].split(':') #get translation line
        if(translation[0] in text):
            match = True

    return match

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")

    return str(text)

def remove_urls(text):
    """
    Removes URLs from input string.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    return re.sub(r'http\S+', '', text)

def replace_words(text):
    """
    Searches text for words contained in ./dic.txt and replaces them.

    :param text: The input string.
    :type text: String.

    :returns: The processed String or "-1" if there is no match
    :rtype: String.
    """
    dic_file = open('./dic.txt', 'r')

    text = remove_urls(text)
    text = strip_accents(text)

    if(not is_match(text)):
        return "-1"

    for line in dic_file.readlines():
        translation = line.split('\n')[0].split(':') #get translation line
        insensitive = re.compile(re.escape(translation[0]), re.IGNORECASE)
        text = insensitive.sub(translation[1], text)

    dic_file.close()

    return text

def is_mention_valid(text):
    """
    Evaluates the validity of a tweet mention.

    :param text: The input string.
    :type text: String.

    :returns: Input string validity.
    :rtype: Boolean
    """
    valid = True

    # Mention starts with @ny_tames
    if(text.split(' ', 1)[0] != "@ny_tames"):
        valid = False

    if(':' not in text.split(' ', 1)[1]):
        valid = False

    return valid
