import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, title, director, storyline, poster_image_url,
                 youtube_trailer_url, genres, year, rating, cast):
        self.title = title
        self.director = director
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.youtube_trailer_url = youtube_trailer_url
        self.genres = genres
        self.year = year
        self.rating = rating
        self.cast = cast
