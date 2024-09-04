def get_music_info ():
    year = input("Enter the year: ")
    Genre = input("Enter the Genre: ")
    Album = input("Enter the the Album: ")
    Title = input("Enter the song title: ")
    Artist = input("Enter the artist: ")
    
    print("------------------------------")
    print("SONG DETAILS")
    print("------------------------------")
    
    print(f"year released: {year}")
    print(f"genre: {Genre}")
    print(f"album: {Album}")
    print(f"title: {Title}")
    print(f"artist: {Artist}")
    
get_music_info()