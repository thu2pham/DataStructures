'''
customproblem import statement
'''
name = "customproblem"

from .customproblem import Movies, Awards, Popular, IndependentMovie, StudioMovie

__all__ = ['Movies', 'Awards', 'Popular', 'IndependentMovie', 'StudioMovie']
