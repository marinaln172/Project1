def get_random_string(length):
    import random
    import string
    
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))
