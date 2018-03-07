import media

def create_home_page_html(movies):
    html = create_home_html_code(movies)
    
    home_page = open("new_fresh_tomatoes.html", "w")
    home_page.write(html)
    home_page.close()

def create_home_html_code(movies):    
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    '''
    
    head = get_head()
    html += head

    body = get_body(movies)
    html += body

    html += "\n\t</html>"
    
    return html

def get_head():
    return '''
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- ICON LIBRARY FROM https://www.w3schools.com/howto/howto_css_star_rating.asp -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <link rel="stylesheet" href="new_fresh_tomatoes.css">
            <title>Fresh Tomatoes - HOME PAGE</title>
        </head>
    '''

def get_body(movies):
    #main part of the page
    html = '''

        <body>
            <!-- MOVIES -->
            <div class="container">
    '''

    movie_number = 0
    for movie in movies:
        html += get_movie_infos(movie, movie_number)
        movie_number += 1
        
    html += "\n\n\t\t\t</div>"

    #trailer container
    html +='''

            <!-- TRAILER CONTAINER -->
            <div id="overlay" onclick="closeOverlay()">
                <iframe id="trailer" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
    '''

    #trailer functions
    html += get_trailer_functions(movies, movie_number)
    
    html += "\n\n\t\t</body>"
    
    return html

def get_movie_infos(movie, movie_number):
    html = "\n\t\t\t\t<div class=\"box\">"
    html += get_poster_code(movie.poster_image_url) + "\n\t\t\t\t\t<span class=\"description main-infos\">"
    html += get_title_code(movie.title) + get_rating_code(movie.rating)
    html += get_director_code(movie.director)
    html += '''
                    </span>
                    <br>
                    <span class="description more-infos"><span class="button" onclick=openOverlay(''' + str(movie_number) + ''')>TRAILER</span> | <a class="button">REVIEWS</a></span>
                </div> 
    '''

    return html

def get_poster_code(poster_image_url):
    return "\n\t\t\t\t\t<img src=\"" + poster_image_url + "\">"

def get_title_code(title):
    return "\n\t\t\t\t\t\t<p><strong>" + title + "</strong></p>"
    
def get_rating_code(rating):
    html = ""
    for star in range(0, rating):
        html += '''
                        <span class="fa fa-star checked"></span>'''
    black_stars_number = 5 - rating
    for black_star in range(0, black_stars_number):
        html += '''
                        <span class="fa fa-star"></span>'''

    return html

def get_director_code(director):
    return "\n\t\t\t\t\t\t<p>" + director + "</p>"

def get_trailer_functions(movies, movie_number):
    html = '''
            <script>
                function openOverlay(movie_number) {
                    document.getElementById("overlay").style.display = "block";
                    playVideo(movie_number);
                }

                function closeOverlay() {
                    document.getElementById("overlay").style.display = "none";
                    stopVideo();
                }

                var trailer_code = ['''

    index = 0
    for movie in movies:
        html += "\"" + get_trailer_code(movie.youtube_trailer_url) + "\""
        index += 1
        if index < movie_number:
            html += ", "

    html += "];"

    html += '''

                function playVideo(movie_number) {
    				document.getElementById("trailer").src = trailer_code[movie_number];
    			}

    			function stopVideo() {
    				document.getElementById("trailer").src = "";
    			}
    			
    	    </script>'''
    
    return html

def get_trailer_code(youtube_trailer_url):
    trailer_code = youtube_trailer_url.replace("watch?v=", "embed/")
    index_of_t_string = trailer_code.find("&t")
    if index_of_t_string > -1:
        delete_by_here = - (len(trailer_code) - index_of_t_string)
        trailer_code = trailer_code[:delete_by_here]
    trailer_code+= "?autoplay=1"
                                        
    return trailer_code
    
