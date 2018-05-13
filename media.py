import webbrowser


class Movie ():
    '''A class to model a movie.

    Attributes:
            title (str): the title of the movie.
            storyline (str): a breif description of the movie.
            image (str): A poster image of the move which is a URL link to a
                         image hosted on wikipedia.
            trailer (str): A URL link to the movies trailer hosted on YouTube.
            '''
    def __init__(self, title, storyline, image, trailer):
        '''Constructor to initialize a movie object with a title, storyline,
           image, and a trailer.'''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        '''Opens a tab in the users default web browser to the home page:
           fresh_tomatoes.html.'''
        webbrowser.open_new_tab(self.trailer_youtube_url)
