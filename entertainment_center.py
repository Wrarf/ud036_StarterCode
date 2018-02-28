import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

spirited_away = media.Movie("Spirited Away",
                     "Tale of the fanciful adventures of a ten-year-old girl named Chihiro, who discovers a secret world",
                     "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
                     "https://www.youtube.com/watch?v=ByXuk9QqQkk")

the_truman_show = media.Movie("The Truman Show",
                              "Truman Burbank is the unsuspecting star of The Truman Show, a reality television program which is broadcast live around the clock and across the globe.",
                              "https://upload.wikimedia.org/wikipedia/en/c/cd/Trumanshow.jpg",
                              "https://www.youtube.com/watch?v=loTIzXAS7v4")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Gil takes a walk at midnight and discovers what could be the ultimate source of inspiration for writing",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

up = media.Movie("Up",
                 "Carl Fredricksen as a boy wanted to explore South America and find the forbidden Paradise Falls. About 64 years later he gets to begin his journey along with a Boy Scout named Russel with help from 500 balloons.",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=kBBsE4TK06U")

birdman = media.Movie("Birdman or (The Unexpected Virtue of Ignorance)",
                      "A washed-up actor, who once played an iconic superhero, attempts to revive his career by writing and starring in his very own Broadway play",
                      "https://upload.wikimedia.org/wikipedia/en/6/63/Birdman_poster.png",
                      "https://www.youtube.com/watch?v=uJfLoE6hanc")

movies = [toy_story, spirited_away, the_truman_show, midnight_in_paris, up, birdman]
fresh_tomatoes.open_movies_page(movies)
