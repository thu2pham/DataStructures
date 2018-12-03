'''
Testing customproblem
'''
#!/usr/bin/python3

import pytest
from projects.customproblem.customproblem import Movies, Awards, Popular, IndependentMovie, StudioMovie

class TestCustomProblemMethods:
    '''Testing module movie'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.movie1 = Movies('The Godfather', 'Crime, Drama', 'Francis Ford Coppola', '1972')
        self.movie2 = Movies('Fight Club', 'Drama', 'David Fincher', '1999')
        self.movie3 = Movies('The Godfather', 'Crime, Drama', 'Francis Ford Coppola', '1972')
        self.award1 = Awards('Oscar', 'Best Picture', self.movie1)
        self.award2 = Awards('Empire', 'Best British Actress', self.movie2)
        self.indie_mov = IndependentMovie(self.award1, 500000.00, 1000000.00)
        self.indie_mov2 = IndependentMovie(self.award1, 500000.00, 1000000.00)
        self.stud_mov = StudioMovie(self.award2, 30, 1200000000.00)
        self.stud_mov2 = StudioMovie(self.award2, 30, 0.00)
        self.popular1 = Popular(self.award1, 500000.00)
        self.popular2 = Popular(self.award1, 300000.00)

    def test_movies(self):
        '''Testing movie properties'''
        assert self.movie1.title == 'The Godfather'
        assert self.movie1.genre == 'Crime, Drama'
        assert self.movie1.director == 'Francis Ford Coppola'
        assert self.movie1.year == '1972'

    def test_movies_str(self, capsys):
        '''Testing movies.__str__ method'''
        print(self.movie1)
        out, err = capsys.readouterr()
        assert out.strip() == ('Title: The Godfather\nGenre: Crime, Drama\nDirector: Francis Ford Coppola\nYear Released: 1972')

    def test_movies_eq(self):
        '''Testing movies.__eq__ method'''
        assert self.movie1 != self.movie2
        assert self.movie1 is not self.movie3
        assert self.movie1 == self.movie3
    
    def test_movies_rated(self, capsys):
        assert self.movie2.rated() == ('The movie is not rated')
  
    def test_movies_release(self, capsys):
        assert self.movie1.release() == ('The movie was released')

    def test_awards(self):
        '''Testing customer properties'''
        assert self.award1.name == 'Oscar'
        assert self.award1.category == 'Best Picture'
        assert self.award1.movie == Movies('The Godfather', 'Crime, Drama', 'Francis Ford Coppola', '1972')

    def test_awards_str(self, capsys):
        '''Testing awards.__str__ method'''
        print(self.award1)
        out, err = capsys.readouterr()
        assert out.strip() == ('Oscar Award\nCategory: Best Picture\n' + 'Title: The Godfather\nGenre: Crime, Drama\nDirector: Francis Ford Coppola\nYear Released: 1972')

    def test_awards_best_picture(self, capsys):
        '''Testing awards.best_picture method'''
        self.award1.best_picture(335, self.movie1)
        assert self.award1.best_picture(335, self.movie1) == ('Best Picture Nominee: ' + 'Title: The Godfather\nGenre: Crime, Drama\nDirector: Francis Ford Coppola\nYear Released: 1972')

    def test_awards_academy(self, capsys):
        assert self.award1.academy_award() == ('This is an Academy Award')

    def test_awards_eq(self):
        '''Testing awards.__eq__ method'''
        assert self.award1 != self.award2

    def test_popular(self):
        '''Testing popular properties'''
        assert self.indie_mov.award == self.award1
        assert self.stud_mov.award == self.award2
        assert self.indie_mov.box_office == pytest.approx(1000000, 0.01)
        assert self.stud_mov.box_office == pytest.approx(1200000000, 0.01)

    def test_popular_eq(self):
        '''Testing popular.__eq__ method'''
        assert self.popular1 != self.popular2

    def test_popular_gross(self):
        '''Testing popular.gross method'''
        self.indie_mov.gross(1000000)
        assert self.indie_mov.box_office == pytest.approx(2000000, 0.01)

    def test_popular_flop(self):
        '''Testing popular.flop method'''
        self.stud_mov2.flop()
        assert self.stud_mov2.box_office == pytest.approx(0, 0.01)

    def test_indie_independent(self):
        '''Testing indie movie independent method'''
        assert self.indie_mov.independent() == ('This is an indie film')

    def test_indie_eq(self):
        '''Testing indie.__eq__ method'''
        assert self.indie_mov == self.indie_mov2

    def test_indie_str(self, capsys):
        '''Testing indie.__str__ method'''
        print(self.indie_mov)
        out, err = capsys.readouterr()
        assert out.strip() == ('Popular Independent Movie:' + 'The movie is popular with Oscar Award\nCategory: Best Picture\n' + 'Title: The Godfather\nGenre: Crime, Drama\nDirector: Francis Ford Coppola\nYear Released: 1972 making 1000000.00 gross')

    def test_indie_blockbuster(self, capsys):
        '''Testing indie.blockbuster method'''
        assert self.indie_mov.blockbuster() == ('This indie movie is not a blockbuster')

    def test_studio_net_collection(self):
        '''Testing net collection method'''
        assert self.stud_mov.box_office == pytest.approx(1200000000.00, 0.01)
        self.stud_mov.net_collection()
        assert self.stud_mov.box_office == pytest.approx(840000000.00, 0.01)

    def test_studio_blockbuster(self, capsys):
        '''Testing studio.blockbuster method'''
        assert self.stud_mov.blockbuster() == ('This movie can be considered a blockbuster')
        
    def test_studio_eq(self):
        '''Testing studio.__eq__ method'''
        assert self.stud_mov != self.stud_mov2

    def test_studio_str(self, capsys):
        '''Testing studio.__str__ method'''
        print(self.stud_mov)
        out, err = capsys.readouterr()
        assert out.strip() == ('Major Studio Movie\n' + 'The movie is popular with Empire Award\n' + 'Category: Best British Actress\n' + 'Title: Fight Club\n' + 'Genre: Drama\n' + 'Director: David Fincher\n' + 'Year Released: 1999 making 1200000000.00 gross')

if __name__ == '__main__':
    pytest.main(['test_customproblem.py'])
