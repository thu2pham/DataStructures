'''
customproblem classes
Thu Pham - Movies Project
'''
#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Movies:
    '''Movies class'''
    def __init__(self, title_init: str, genre_init: str, director_init: str, year_init: str):
        '''__init__'''
        self._title = title_init
        self._genre = genre_init
        self._director = director_init
        self._year = year_init

    # TODO: Implement data members as properties
    @property
    def title(self):
        return self._title
    @title.setter
    def title_init(self, new_value):
        self._title = new_value
    
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, new_value):
        self._genre = new_value
    
    @property
    def director(self):
        return self._director
    @director.setter
    def director(self, new_value):
        self._director = new_value
    
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, new_value):
        self._year = new_value

    def __eq__(self, other: object):
        '''Compare 2 movies'''
        if self._title == other._title and self._genre == other._genre and self._director == other._director and self._year == other._year:
            return True
        else:
            return False

    def rated(self):
        if self._genre == 'Drama':
            return "The movie is not rated"

    def release(self):
        if int(self._year) < 2018:
            return "The movie was released"
        else:
            return "The movie is not released yet"

    def __str__(self):
        '''__str method'''
        return "Title: {}\nGenre: {}\nDirector: {}\nYear Released: {}".format(self._title, self._genre, self._director, self._year)

class Awards():
    '''Awards class'''
    def __init__(self, name_init: str, category_init: str, movie_init: object):
        '''Constructor'''
        self._name = name_init
        self._category = category_init
        self._movie = movie_init

    # TODO: Implement data members as properties
    @property
    def name(self):
        return self._name
    @name.setter
    def year(self, new_value):
        self._name = new_value
    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_value):
        self._category = new_value

    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, new_value):
        self._movie = new_value

    def __eq__(self, other: object):
        '''Compare 2 awards'''
        if self._name == other._name and self._category == other._category and self._movie == other._movie:
            return True
        else:
            return False

    def best_picture(self, votes: int, nominee: object):
        '''Movie to be nominated as Best Picture '''
        if votes >= 333:
            self._movie = nominee
            return "Best Picture Nominee: {}".format(self._movie)

    def academy_award(self):
        if self._name == 'Oscar':
            return "This is an Academy Award"

    def __str__(self):
        '''__str'''
        return "{} Award\nCategory: {}\n{}".format(self._name, self._category, self._movie)


class Popular(ABC):
    '''Popular class'''
    # @abstractmethod
    def __init__(self, award_init: object, box_office_init: float=0):
        '''Constructor'''
        self._award = award_init
        self._box_office = box_office_init

    # TODO: Implement data members as properties
    @property
    def award(self):
        return self._award
    @award.setter
    def award(self, new_value):
        self._award = new_value
    
    @property
    def box_office(self):
        return self._box_office
    @box_office.setter
    def rating(self, new_value):
        self._box_office= new_value

    def __eq__(self, other: object):
        '''Compare 2 popular awarded movies'''
        if self._award == other._award and self._box_office == other._box_office: 
            return True
        else:
            return False

    def gross(self, amount: float):
        ''' Does the movie make any profit'''
        if amount > 0:
            self._box_office += amount
            return self._box_office
        else:
            raise ValueError('The movie does not make any profit')

    def flop(self):
        '''A flop movie'''
        self._box_office <= 0
        
    def __str__(self):
        '''__str__'''
        return "The movie is popular with {} making {:.2f} gross".format(self._award, self._box_office)

class IndependentMovie(Popular):
    '''IndependentMovie class'''
    def __init__(self, award_init: object, budget_init: float, gross_init: float=0):
        '''Constructor'''
        super().__init__(award_init, gross_init)
        self._budget = budget_init

    def __eq__(self, other: object):
        '''Compare 2 popular indie movies'''
        if self._award == other._award and self._budget == other._budget and self._box_office == other._box_office: 
            return True
        else:
            return False

    def independent(self):
        '''Define an indie movie'''
        if self._budget >= 20000000:
            return "This is not an indie film"
        else:
            return "This is an indie film"    

    def blockbuster(self):
        '''Define an indie blockbuster'''
        if self._box_office / self._budget >= 10000:
            return "This is an indie blockbuster"
        else:
            return "This indie movie is not a blockbuster"
        
    def __str__(self):
        '''__str__'''
        return "Popular Independent Movie:" + super().__str__()


class StudioMovie(Popular):
    '''StudioMovie class'''
    def __init__(self, award_init: object, entertainment_tax_init: float, gross_init: float=0):
        '''Constructor'''
        super().__init__(award_init, gross_init)
        self._entertainment_tax = entertainment_tax_init        

    def net_collection(self):
        '''Net Collection after Tax'''
        self._entertainment_tax = self._box_office * self._entertainment_tax/100
        self._box_office = self._box_office - self._entertainment_tax
        return self._box_office

    def blockbuster(self):
        if self._box_office >= 100000000:
            return "This movie can be considered a blockbuster"

    def __eq__(self, other: object):
        '''Compare 2 popular studio movies'''
        if self._award == other._award and self._entertainment_tax == other._entertainment_tax and self._box_office == other._box_office: 
            return True
        else:
            return False 

    def __str__(self):
        '''__str__'''
        return "Major Studio Movie\n" + super().__str__()
        

