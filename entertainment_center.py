from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story",
                 "A story about a boys toys coming to life.",
                 "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                 "https://www.youtube.com/watch?v=Ny_hRfvsmU8")

avatar = Movie("Avatar", 
               "A marine on an alien planet tries to save the aliens from other humans.",
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

fight_club = Movie("Fight Club", 
                   "A man fights back against the soul crushing american society.",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                   "https://www.youtube.com/watch?v=SUXWAEX2jlg") 

school_of_rock = Movie("School of Rock", 
                       "Struggling Musician does a bad job teaching kids.",
                       "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                       "https://www.youtube.com/watch?v=XCwy6lW5Ixc") 

hunger_games = Movie("Hunger Games",
                     "A women enter a competition to fight to the death with other people.",
                     "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8") 

wreck_it_ralph = Movie("Wreck it Ralph",
                       "A video game character fights to save other video game characters.",
                       "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg",
                       "https://www.youtube.com/watch?v=87E6N7ToCxs")        

movies = [toy_story, avatar, fight_club, school_of_rock, hunger_games, wreck_it_ralph]

fresh_tomatoes.open_movies_page(movies)