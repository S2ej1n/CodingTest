def solution(phone_book):
    phone_book.sort()
    
    for p, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p):
            return False
    return True