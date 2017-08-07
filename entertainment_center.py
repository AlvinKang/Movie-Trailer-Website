import media
import fresh_tomatoes

# Create 6 Movie objects
inception_movie = media.Movie("Inception",
							  "A man and his team goes into others' dreams",
							  "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
							  "https://www.youtube.com/watch?v=YoHD9XEInc0")

zootopia_movie = media.Movie("Zootopia",
							 "A bunny and fox team up to solve the myster of Zootopia",
							 "https://s-media-cache-ak0.pinimg.com/originals/5a/29/d7/5a29d758e586fa4c44ef0e9065b4651c.jpg",
							 "https://www.youtube.com/watch?v=CzvH6_e2a-U")

forrest_gump_movie = media.Movie("Forrest Gump",
								 "Autistic man lives through numerous historical events",
								 "http://www.impawards.com/1994/posters/forrest_gump_xlg.jpg",
								 "https://www.youtube.com/watch?v=bLvqoHBptjg")

walle_movie = media.Movie("Wall-E",
						  "A robot couple brings humanity back to Earth",
						  "https://img.yescdn.ru/2015/09/15/poster/WALL-E_1.jpg",
						  "https://www.youtube.com/watch?v=ZAWIIlXNGwY")

lotr_movie = media.Movie("The Lord of the Rings: Return of the King",
						 "The third and final movie to the LOTR trilogy",
						 "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
						 "https://www.youtube.com/watch?v=y2rYRu8UW8M")

potc_movie = media.Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
						"A pirate and his crew set sail for the cursed treasure of the Caribbean",
						"http://mrhipster.com/wp/wp-content/uploads/2015/02/pirates-of-the-caribbean-curse-of-the-black-pearl.jpg",
						"https://www.youtube.com/watch?v=naQr0uTrH_s")

movies = [inception_movie, zootopia_movie, forrest_gump_movie, walle_movie, lotr_movie, potc_movie]
fresh_tomatoes.open_movies_page(movies)