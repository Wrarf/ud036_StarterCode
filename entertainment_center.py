# -*- coding: cp1252 -*-
import media
import fresh_tomatoes

standard_reviews = ["Nice film", "I liked it"]

up = media.Movie("Up",
                 "Pete Docter",
                 "After the death of his wife and an incident at home, an old man, Carl Fredericksen, is forced into a retirement home. However, he still wants to go on the adventure to South America he and his wife planned.Ultimately, the adventure involves a flying house, a young boy, a talking dog and a strange, large bird.",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=qas5lWp7_R0&t=1s",
                 ["adventure", "animation", "family", "comedy"],
                 "2009",
                 5,
                 [],
                 standard_reviews)

howls_moving_castle = media.Movie("Howl's Moving Castel",
                                  "Hayao Miyazaki",
                                  "When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.",
                                  "https://fiu-assets-2-syitaetz61hl2sa.stackpathdns.com/static/use-media-items/17/16574/upto-700xauto/56702d32/Howls_Moving_Castle-Olly_Moss.jpeg?resolution=0",
                                  "https://www.youtube.com/watch?v=iwROgK94zcM",
                                  ["animation", "drama", "fantasy", "science fiction", "romance"],
                                  "2005",
                                  4,
                                  [],
                                  standard_reviews)

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Woody Allen",
                                "Gil takes a walk at midnight and discovers what could be the ultimate source of inspiration for writing",
                                "https://eu.movieposter.com/posters/archive/main/145/MPW-72510",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY&t=1s",
                                ["comedy", "romance"],
                                "2011"
                                5,
                                ["Owen Wilson", "Rachel McAdams", "Kathy Bates"],
                                standard_reviews)

toy_story_3 = media.Movie("Toy Story 3",
                          "Lee Unkrich",
                          "Andy is going to college and doesn't play with his toys anymore causing Woody and the others to be donated to Sunnyside Daycare, where they discover that the place is not exactly what they dreamed it was, and will have to face many dangers to come home safely.",
                          "http://images6.fanpop.com/image/photos/40100000/Toy-Story-3-The-Great-Escape-Poster-pixar-40152166-354-500.jpg",
                          "https://www.youtube.com/watch?v=ZZv1vki4ou4",
                          ["animation", "comedy"],
                          "2010",
                          5,
                          [],
                          standard_reviews)

spotless_mind = media.Movie("Eternal Sunshine of the Spotless Mind",
                            "Michel Gondry",
                            "A man, Joel Barish, heartbroken that his girlfriend Clementine underwent a procedure to erase him from her memory, decides to do the same. However, as he watches his memories of her fade away, he realizes that he still loves her, and may be too late to correct his mistake.",
                            "https://i.pinimg.com/564x/67/25/3c/67253cb97e3827cc3738c4140f9c9891.jpg",
                            "https://www.youtube.com/watch?v=hj7Wgd_Yn94",
                            ["comedy", "drama", "science fiction", "romance"],
                            "2004",
                            5,
                            ["Jim Carrey", "Kate Winslet", "Kirsten Dunst", "Mark Ruffalo", "Elijah Wood", "Tom Wilkinson"],
                            standard_reviews)

grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                                   "Wes Anderson",
                                   "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
                                   "http://poolga.com/shared/images/poolgas/iphone_2032.jpg",
                                   "https://www.youtube.com/watch?v=1Fg5iWmQjwk",
                                   ["comedy", "drama"],
                                   "2014",
                                   4,
                                   ["Ralph Fiennes", "Tony Revolori", "F. Murray Abraham"],
                                   standard_reviews)

birdman = media.Movie("Birdman or (The Unespected Virtue of Ignorance)",
                      "Alejandro González Iñárritu",
                      "A washed-up actor, who once played an iconic superhero, attempts to revive his career by writing and starring in his very own Broadway play.",
                      "https://pre00.deviantart.net/6308/th/pre/f/2015/160/3/a/birdman_vector_poster_by_metalraj-d8wpn4q.jpg",
                      "https://www.youtube.com/watch?v=uJfLoE6hanc&t=4s",
                      ["comedy", "drama"],
                      "2014",
                      5,
                      ["Michael Keaton", "Edward Norton", "Zach Galifianakis", "Emma Stone"],
                      standard_reviews)

movies = [toy_story, spirited_away, the_truman_show, midnight_in_paris, up, birdman]
#fresh_tomatoes.open_movies_page(movies)
