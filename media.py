import webbrowser 

class Movie():
    """ This class provides a way to store movie related information """
    
    def __init__(self, title, storyline, poster_image_url,
                 youtube_trailer_url, genre, year, rating, cast, reviews):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.youtube_trailer_url = youtube_trailer_url
        self.genre = genre
        self.year = year
        self.rating = rating
        self.cast = cast
        self.reviews = reviews
