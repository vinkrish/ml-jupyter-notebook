# composition is a design principle where a class is composed of one or more objects of other classes. 
# Instead of using inheritance (i.e., "is-a" relationship), composition represents a "has-a" relationship.

# Basic Composition
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine):
        self.engine = engine  # Car "has-a" Engine

    def drive(self):
        return f"Car is driving. {self.engine.start()}"

# Example usage
engine = Engine()
car = Car(engine)
print(car.drive())  # Output: Car is driving. Engine started.

# Composition with Multiple Objects
class Battery:
    def charge(self):
        return "Battery charged."

class ElectricMotor:
    def run(self):
        return "Electric motor running."

class ElectricCar:
    def __init__(self, battery, motor):
        self.battery = battery
        self.motor = motor

    def drive(self):
        return f"{self.battery.charge()} {self.motor.run()}"

# Example usage
battery = Battery()
motor = ElectricMotor()
electric_car = ElectricCar(battery, motor)
print(electric_car.drive())  # Output: Battery charged. Electric motor running.

# Composition for Reusability
class Screen:
    def display(self, message):
        return f"Displaying: {message}"

class Speaker:
    def play_sound(self):
        return "Playing sound."

class Smartphone:
    def __init__(self, screen, speaker):
        self.screen = screen
        self.speaker = speaker

    def use(self):
        return f"{self.screen.display('Hello World')} {self.speaker.play_sound()}"

# Example usage
screen = Screen()
speaker = Speaker()
phone = Smartphone(screen, speaker)
print(phone.use())  # Output: Displaying: Hello World. Playing sound.

# Composition with a List of Objects
class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        return [f"Playing: {song.title}" for song in self.songs]

# Example usage
song1 = Song("Song 1")
song2 = Song("Song 2")
playlist = Playlist()
playlist.add_song(song1)
playlist.add_song(song2)

print(playlist.play_all())  # Output: ['Playing: Song 1', 'Playing: Song 2']

# using *args syntax to accept variable number of Song objects
class Song2:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Song: {self.title}"

class Playlist2:
    def __init__(self, *songs):
        # Initialize the playlist with the provided songs
        self.songs = list(songs)

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        return [f"Playing: {song.title}" for song in self.songs]

    def __str__(self):
        return f"Playlist: {[song.title for song in self.songs]}"

# Example usage
song21 = Song2("Song 1")
song22 = Song2("Song 2")
song23 = Song2("Song 3")

# Creating a playlist with a variable number of Song objects
playlist2 = Playlist2(song21, song22, song23)
print(playlist2)  # Output: Playlist: ['Song 1', 'Song 2', 'Song 3']

# Playing all songs in the playlist
print(playlist2.play_all())  # Output: ['Playing: Song 1', 'Playing: Song 2', 'Playing: Song 3']

# Adding another song
song24 = Song2("Song 4")
playlist2.add_song(song24)
print(playlist2)  # Output: Playlist: ['Song 1', 'Song 2', 'Song 3', 'Song 4']
