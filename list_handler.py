import random

def choose_keywords(n: int, keywords:list) -> list:
    random.shuffle(keywords)
    if keywords.__len__() < n:
        print("Requested Searching reps is larger than available keywords.")
        print("Available keywords:", keywords.__len__())
        print("Requested reps:    ", n)
        while True:
            user_choice = input("Would you like to continue?(y/n) ")
            
            if user_choice == ('y' or 'Y'):
                return keywords
            elif user_choice == ('n' or 'N'):
                return []
            else:
                print("Invalid choice.")
    else:
        if n <= 0:
            return []
        return keywords[:n]
    