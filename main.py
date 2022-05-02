from turtle import tilt, title
import random
from datetime import date

today = date.today().strftime('%d/%m/%Y')

print("BIBLIOTEKA FILMOW I SERIALI")

#Utworzenie klasy movie
class movie:
    def __init__(self, title, date, genre, number_plays):
        self.title = title
        self.date = date
        self.genre = genre
        self.numbers_plays = number_plays

    def __str__(self):
        return f'{self.title}, został wydany w: {self.date} roku.'
    def __repr__(self):
        return f"\n {self.title} {self.date} {self.genre} {self.numbers_plays}"
    def play (self, step = 1):
        self.numbers_plays += step

#Rozszerzenie klasy movie o serials
class serials(movie):
    def __init__(self,episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    def __str__(self):
        return f'{self.title} S{self.season_number:02d}E{self.episode_number:02d}'

#Biblioteka filmów
Godfather = movie(title="Godfather", date=1972, genre="Drama", number_plays=0)
Godfather_2 = movie(title="Godfather II", date=1974, genre="Drama", number_plays=0)
Inception = movie(title="Inception", date=2011, genre="Sci-Fi", number_plays=0)
TheDevilsAdvocate = movie(title="The Devil's Advocate", date=1997, genre="Thriller", number_plays=0)
Kiler = movie(title="Kiler", date=1997, genre="Comedy", number_plays=0)
PiratesOfTheCaribbean_1 =  movie(title="Pirates of the Caribbean: Dead Man's Chest", date=2007, genre="Adventure", number_plays=0)
TheLionKing = movie(title="The Lion King", date=1999, genre="Family", number_plays=0)

#Biblioteka seriali
Lucifer = serials(title="Lucifer", date=2016, genre="Fantasy",season_number=1,episode_number=1, number_plays=0)
The100 = serials(title="The100", date=2014, genre="Sci-Fi",season_number=1,episode_number=1, number_plays=0)
StrangerThing = serials(title="Stranger Thing", date=2016, genre="Fantasy",season_number= 1 ,episode_number= 1 , number_plays=0)
GameOfThrones = serials(title="Game Of Throne", date=2011, genre="Fantasy",season_number= 1 ,episode_number= 1 , number_plays=0)
TheWitcher = serials(title="The Witcher", date=2020, genre="Fantasy",season_number= 1 ,episode_number= 1 , number_plays=0)
Suits = serials(title="Suits", date=2011, genre="Comedy",season_number= 1 ,episode_number= 1 , number_plays=0)
Sherlock = serials(title="Sherlock", date=2016, genre="Detective story",season_number= 1 ,episode_number= 1 , number_plays=0)

#Lista filmów i seriali
List = [Godfather, Godfather_2, Lucifer, The100, StrangerThing, Inception, TheDevilsAdvocate, Kiler, GameOfThrones, TheWitcher, PiratesOfTheCaribbean_1, TheLionKing, Suits, Sherlock]
List_movie = []
List_serials = []

#print(isinstance(Kiler, movie))
#print(isinstance(Kiler, serials))

#Sprawdzenie czy tytuł to serial czy film
def Movie_or_Serial ():
    for i in range (0, len(List)):
        movie_or_serial = isinstance(List[i], serials)
        if movie_or_serial == True:
            List_serials.append(List[i])
        else:
            List_movie.append(List[i])

#Wyswietlenie tylko filmów/seriali            
def get_movie():
    List_movie.clear()
    Movie_or_Serial()
    List_movie_sorted = sorted(List_movie, key=lambda movie: movie.title)
    print(List_movie_sorted)
    List_serials =[]

def get_serial():
    List_serials.clear()
    Movie_or_Serial()
    List_serials_sorted = sorted(List_serials, key=lambda serials: serials.title)
    print(List_serials_sorted)

#JAK ZROBIĆ ZEBY NIE WYSYPYWAŁ SIĘ PRZY 78 LINII KIEDY NIE MA TAKIEGO TYTULU?
def search():

    tytul = input("Podaj tytuł filmu który chcesz wyszukać: ")
    tytul_obj = eval(tytul)
    if isinstance(tytul_obj, serials) or isinstance(tytul_obj, movie) == True:
        print(tytul_obj) 
    else:
        "Nie ma takiego filmu czy też serialu!"

#Generowanie losowej (od 0 do 100) liczby wyświetleń, dla losowego filmu.
#LEN LIST - 1 bo zaczynamy liczyć od 0 !!!!!
def generate_views():
    wylosowany = (List[random.randint(0, len(List)-1)]) 
    wylosowany.play(random.randint(1,100))
    #print(f"{wylosowany} Dodano: {wylosowany.numbers_plays} odtworzeń")

#Użycie 10 razy funkcji generate_views
def views_x10():
    for i in range(0,9):
        generate_views()

#Wyszukanie listy TOP3 filmów i seriali.
def top_views():
    views_x10()
    top3 = sorted(List, key=lambda movie: movie.numbers_plays, reverse = True)
    print(f"Najpopularniejsze TOP3 produkcje na dzień  {today} :")
    print(f" TOP1: {top3[0].title} z {top3[0].numbers_plays} wyświetleniami")
    print(f"  TOP2:  {top3[1].title} z {top3[1].numbers_plays} wyświetlenami")
    print(f"   TOP3:   {top3[2].title} z {top3[2].numbers_plays} wyświetlenami")

top_views()

#DOKONCZYĆ - zadania dla chętnych