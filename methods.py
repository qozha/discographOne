def popularity(json):
    try:
        return int(json['popularity'])
    except KeyError:
        return 0


def get_popularity(json, sp):
    track_uris = []
    for track in json:
        track_uris.append(track['id'])
    return sp.tracks(track_uris)


def get_popular_tracks(albums, sp):
    best_tracks = []
    previous_album = ''
    for album in albums:
        tracks = sp.album_tracks(album['id'])['items']
        tracks = get_popularity(tracks, sp)['tracks']
        tracks.sort(key=popularity, reverse=True)
        if(album['name'] != previous_album):
            best_tracks.append(tracks[0])
            print(album['name'] + "'s most popular song is: " +
                  tracks[0]['name'])
        previous_album = album['name']
    return best_tracks


def get_discographone_playlist(sp, name):

    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]

    albums = sp.artist_albums(artist['id'])['items']

    try:
        albums.sort(key=lambda x: x['release_date'])
    except:
        pass

    return get_popular_tracks(albums, sp)


def get_tracks_uris(tracks):
    uris = []
    for track in tracks:
        uris.append(track['id'])
    return uris


def create_discographone_playlist(spoty, tracks, name):
    user = spoty.me()
    playlist_name = name + "'s DiscographOne"
    playlist_uri = spoty.user_playlist_create(user['id'], playlist_name)['uri']

    uris = get_tracks_uris(tracks)

    spoty.playlist_add_items(playlist_uri, uris)

    return True
