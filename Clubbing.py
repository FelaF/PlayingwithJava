def enter_club(name: str, age: int, has_id:bool) -> None:
    if name.lower() == 'bob':
        print('Get out of here Bob, we don\'t want no trouble')
        return
    
    if age >= 21 and has_id:
        print('You may enter the club.')
    else:
        print('You may not enter the club.')


def ClubbingFunction() -> None:
    enter_club('Jimmy', 29, has_id=False)
    enter_club('James', 22, has_id=True)
    enter_club('bob' , 21, has_id=True)

if __name__ == '__main__':
    ClubbingFunction()
    print(__name__)
