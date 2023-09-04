
current_movies = {
    'Oppenheimer': '10:00am',
    'Barbie': '11:45am',
    'The Stranger Things': '2:00pm',
    'Dinobots': '5:15pm',
    'McImperium': '9:15pm',        
}

print("Currentl we are showing following movies:\n")
for key in current_movies:
    print(key)

movie = input("What movie would you like to showtime for?\n")
showtime = current_movies.get(movie)

if showtime == None:
    print(f"Sorry Gaffer, we are not playing {movie}. Try pickup something else, please.")
else:
    print(f"{movie} is playing at: {showtime}")