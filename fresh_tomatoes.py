import media
import home_page_html_generator
import home_page_css_generator

def open_movies_page(movies):
    home_page_html_generator.create_home_page_html(movies)
    home_page_css_generator.create_home_page_css()
