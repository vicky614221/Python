class Movies:
    def __init__(self,movie_name,language,release_date):
        self.movie_name = movie_name.upper()
        self.language = language.upper()
        self.release_date = release_date

class Crew(Movies):
    def __init__(self,movie_name,language,release_date,director,producer,cast,music_composer,lyricist,choreographer,singer):
        super().__init__(movie_name,language,release_date)
        self.director = director.upper()
        self.producer = producer.upper()
        self.cast = cast
        self.music_composer = music_composer
        self.lyricist = lyricist
        self.choreographer = choreographer
        self.singer = singer

obj1_crew = Crew()
obj1_movies = Movies()



