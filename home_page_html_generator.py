import media

title = []
director = []
storyline = []
poster_image_url = []
genres = []
year = []
rating = []
cast = []

infos = {0: title,
         1: director,
         2: year,
         3: poster_image_url,
         4: genres,
         5: cast,
         6: rating,
         7: storyline
         }

infos_names = {0: "title",
               1: "director",
               2: "year",
               3: "poster_image_url",
               4: "genres",
               5: "cast",
               6: "rating",
               7: "storyline"
               }


def create_home_page_html(movies):
    html = create_home_html_code(movies)

    home_page = open("fresh_tomatoes.html", "w")
    home_page.write(html)
    home_page.close()


def create_home_html_code(movies):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    '''

    html += get_head()
    html += get_body(movies)

    html += "\n\t</html>"

    return html


def get_head():
    html = '''
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,'''
    html += " initial-scale=1.0\">"
    html += '''
            <link rel="stylesheet" href="fresh_tomatoes.css">
            <title>Fresh Tomatoes - HOME PAGE</title>
        </head>
    '''

    return html


def get_body(movies):
    # main part of the page
    html = '''

        <body>
            <!-- MOVIES -->
            <div class="container">
    '''

    # movie_number is the number of movies in entertainment_center.py
    movie_number = 0
    for movie in movies:
        get_movie_infos(movie)
        html += get_movie_infos_code(movie_number)
        movie_number += 1

    html += "\n\t\t\t</div>"

    # trailer and reviews container
    html += '''

            <!-- TRAILER AND REVIEWS CONTAINER -->
            <div id="overlay" onclick="closeOverlay()">
                <iframe id="trailer" src="" frameborder="0" allow="autoplay;'''
    html += "encrypted-media\" allowfullscreen></iframe>"
    html += '''
               <div id="reviews-container">
    '''

    # builds the structure of the reviews
    for i in range(0, 8):
        if infos_names[i] != "poster_image_url" and infos_names[i] != "rating":
            html += "\n\t\t\t\t\t<p id=\"" + infos_names[i] + "\"></p>"

    html += '''
                    <p id="reviews-message">There are no reviews.</p>
                </div>
            </div>
    '''

    # trailer and reviews infos/functions
    html += "\n\n\t\t\t<script>"
    html += get_variables_code(movies, movie_number)
    html += get_trailer_functions(movies, movie_number)
    html += get_reviews_functions()
    html += "\n\t\t\t</script>"

    html += "\n\n\t\t</body>"

    return html


def get_movie_infos_code(movie_number):
    # html code for the movie boxes
    html = "\n\t\t\t\t<div class=\"box\">"
    html += get_poster_code(poster_image_url[movie_number]) + \
        "\n\t\t\t\t\t<span class=\"description main-infos\">"
    html += get_title_code(title[movie_number]) + \
        get_rating_code(rating[movie_number])
    html += get_director_code(director[movie_number])
    html += '''
                    </span>
                    <br>
                    <span class="description more-infos">'''
    html += '''<span class="button" onclick=playVideo(''' + \
        str(movie_number) + ''')>TRAILER</span>'''
    html += " | <span class=\"button\" onclick=openReviews(" + str(
        movie_number) + ")>REVIEWS</span></span>"
    html += "\n\t\t\t\t</div>\n"

    return html


def get_movie_infos(movie):
    # gets infos of the movies and puts them in the global variables
    title.append(movie.title)
    director.append(movie.director)
    storyline.append(movie.storyline)
    poster_image_url.append(movie.poster_image_url)
    genres.append(movie.genres)
    year.append(movie.year)
    rating.append(movie.rating)
    cast.append(movie.cast)


def get_poster_code(poster_image_url):
    return "\n\t\t\t\t\t<img src=\"" + poster_image_url + "\">"


def get_title_code(title):
    return "\n\t\t\t\t\t\t<p><strong>" + title + "</strong></p>"


def get_rating_code(rating):
    # gives to movies their star rating
    html = ""
    for star in range(0, rating):
        html += '''
                        <span class="star checked">★</span>'''
    black_stars_number = 5 - rating
    for black_star in range(0, black_stars_number):
        html += '''
                        <span class="star">★</span>'''

    return html


def get_director_code(director):
    return "\n\t\t\t\t\t\t<p>" + director + "</p>"


def get_variables_code(movies, movie_number):
    html = ""

    # stores in a javascript list all trailer urls
    html += "\n\t\t\t\tvar trailer_code = ["
    index = 0
    for movie in movies:
        html += "\"" + get_trailer_code(movie.youtube_trailer_url) + "\""
        index += 1
        if index < movie_number:
            html += ", "

    html += "];"

    # stores other movie informations in javascript lists
    for i in range(0, 8):
        if infos_names[i] != "poster_image_url" and infos_names[i] != "rating":
            html += "\n\n\t\t\t\tvar " + infos_names[i] + " = ["
            for j in range(0, movie_number):
                if type(infos[i][j]) is list:
                    html += "["
                    for k in range(0, len(infos[i][j])):
                        html += "\"" + infos[i][j][k] + "\""
                        if k < len(infos[i][j]) - 1:
                            html += ", "
                    html += "]"
                else:
                    html += "\"" + str(infos[i][j]) + "\""
                if j < movie_number - 1:
                    html += ", "
            html += "];"

    return html


def get_trailer_functions(movies, movie_number):
    # javascript functions to play trailers
    html = '''

                function openOverlay() {
                    document.getElementById("overlay").style.display = "block";
                }

                function closeOverlay() {
                    document.getElementById("overlay").style.display = "none";
                    stopVideo();
                    closeReviews();
                }
    '''

    html += '''

                function playVideo(movie_number) {
                    openOverlay();
                    document.getElementById("trailer").src = '''
    html += '''trailer_code[movie_number];
                }

                function stopVideo() {
                    document.getElementById("trailer").src = "";
                }
    '''

    return html


def get_trailer_code(youtube_trailer_url):
    # changes the url of the video to an embedded url
    trailer_code = youtube_trailer_url.replace("watch?v=", "embed/")
    index_of_t_string = trailer_code.find("&t")
    if index_of_t_string > -1:
        delete_by_here = - (len(trailer_code) - index_of_t_string)
        trailer_code = trailer_code[:delete_by_here]
    trailer_code += "?autoplay=1"

    return trailer_code


def get_reviews_functions():
    # javascript functions to show reviews
    html = '''
                function openReviews(movie_number) {
                    openOverlay();
                    get_movie_infos(movie_number);
                    document.getElementById("reviews-container")'''
    html += '''.style.display = "block";
                }

                function get_movie_infos(movie_number) { '''

    for i in range(0, 8):
        if infos_names[i] != "poster_image_url" and infos_names[i] != "rating":
            html += "\n\t\t\t\t\tdocument.getElementById(\"" + infos_names[
                i] + "\").innerHTML = " + infos_names[i] + "[movie_number];"

    html += "\n\t\t\t\t}"

    html += '''

                function closeReviews() {
                    document.getElementById("reviews-container")'''
    html += '''.style.display = "none";
                }'''

    return html
