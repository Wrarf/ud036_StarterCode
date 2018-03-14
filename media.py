import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, title, director, storyline, poster_image_url,
                 youtube_trailer_url, genres, year, rating, cast):
        self.title = title  # string
        self.director = director  # string
        self.storyline = storyline  # string
        self.poster_image_url = poster_image_url  # string
        self.youtube_trailer_url = youtube_trailer_url  # string
        self.genres = genres  # list of strings
        self.year = year  # string
        self.rating = rating  # int
        self.cast = cast  # list of strings
