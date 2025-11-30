import file_handler
import random

def choose_keywords(n: int, filepath: str) -> list:
    kws = file_handler.keywords_load(filepath) or []
    kws = list(kws)
    if kws.__len__() > n:
        print("Requested Searching reps is larger than available keywords. Returning all keywords.")
        return kws
    else:
        random.shuffle(kws)
        if n <= 0:
            return []
        return kws[:n]