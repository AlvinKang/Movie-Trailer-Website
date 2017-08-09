class Movie():

	# Constructor
	def __init__(self, movie_title, movie_summary,
				 movie_poster_url, movie_trailer_url):
		"""
		Creates a Movie object with title, summary, poster image, and link to
		trailer. All arguments take in string inputs.

		Args:
			movie_title (str): Title of movie
			movie_summary (str): Summary of movie
			movie_poster_url (str): URL to movie poster image
			movie_trailer_url (str): URL to movie trailer, preferrably YouTube
		"""
		self.movie_title = movie_title
		self.movie_summary = movie_summary
		self.movie_poster_url = movie_poster_url
		self.movie_trailer_url = movie_trailer_url
