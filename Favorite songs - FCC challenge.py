

def favorite_songs(playlist):

    sorted_playlist = sorted(playlist, key=lambda song: song["plays"])[::-1]

    return [songs["title"] for songs in sorted_playlist][:2]



print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))




