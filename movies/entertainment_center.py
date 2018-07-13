import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#toy_story.show_trailer()

i_robot = media.Movie("I, Robot",
                     "Het verhaal speelt zich af in Chicago in het jaar 2035. Akiva Goldsman besloot later nog een aantal elementen uit een verzameling verhalen van Isaac Asimov, genaamd \"I, Robot\", te integreren in de film. Er worden bijvoorbeeld de drie wetten van de robotica gebruikt en ook komt het Positronisch brein aan bod.",
                     "https://www.movieposter.com/posters/archive/main/238/MPW-119175",
                     "https://www.youtube.com/watch?v=rL6RRIOZyCM")

ratatouille = media.Movie("Ratatouille",
                          "A rat is achef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                           "a really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
movies = [toy_story, avatar, i_robot, ratatouille, hunger_games, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
