import argparse
import json
import requests


KEYWORDS = [
    'river',
    'love',
    'blues',
    'party',
    'time',
    'tonight',
    'rain',
    'morning',
    'breathe',
    'fire',
    'woman',
    'disco',
    'rock',
    'music',
    'dancin',
    'baby',
    'twist',
    'lonely',
    'stop',
    'boogie',
    'christmas',
    'moon',
]


def main():
    parser = initialise_parser()
    args = vars(parser.parse_args())

    args = {key: value for key, value in args.items() if value is not None}

    if not args:
        print("Must use one arg.")
        exit()

    request_params = {
        'track_criteria': {},
        'total_duration': args['total_duration']
    }

    del args['total_duration']

    if 'tolerance_window' in args.keys():
        request_params['tolerance_window'] = args['tolerance_window']
        del args['tolerance_window']

    if 'include_tracks_at' in args.keys():
        tracks_to_include_path = args['include_tracks_at']
        del args['include_tracks_at']

        with open(tracks_to_include_path, 'r') as tracks_file:
            request_params['tracks_to_include'] = json.load(tracks_file)

    for key in args.keys():
        new_key = key.replace('-', '_')
        request_params['track_criteria'][new_key] = args[key]

    del args

    response = requests.post(
        'http://localhost:8000/api/generate/',
        json=request_params,
    )

    if not response.ok:
        print(f'Error: {response.status_code}\nMessage: {response.json()}')
        exit()

    playlist_data = response.json()

    minutes, seconds = convert_minutes(playlist_data['total_duration'])

    print(f'Playlist length: {minutes}:{seconds}')
    print('Track listing:')

    tracks = playlist_data['tracks']
    for i in range(len(tracks)):
        print(f'Track {i+1}')
        track = tracks[i]
        mins, secs = convert_minutes(track['duration'] / 60000)
        print(f'\tTitle: {track["title"]}')
        print(f'\tArtist: {track["artist"]}')
        print(f'\tAlbum: {track["album"]}')
        print(f'\tTrack Position: {track["position"]}')
        print(f'\tOriginal Artist: {track["original_artist"]}')
        print(f'\tDuration: {mins}:{secs}')

    print('\nThanks for using! :)')


def initialise_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--original-artist',
        help='Search for tracks with the same original artist',
        required=False,
    )
    parser.add_argument(
        '--year',
        help='Search for tracks released in the same year.',
        type=int,
        required=False,
    )
    parser.add_argument(
        '--track-number',
        help='Search for tracks with the same track number.',
        required=False,
    )
    parser.add_argument(
        '--keyword',
        help='Search for tracks with a specified keyword in the title.',
        choices=KEYWORDS,
        required=False,
    )
    parser.add_argument(
        '--total-duration',
        help='The length of the playlist you would like to generate.',
        type=int,
    )
    parser.add_argument(
        '--include-tracks-at',
        help=(
            'Path to a JSON file contain tracks you would like to be included.'
        ),
        required=False,
    )
    parser.add_argument(
        '--tolerance-window',
        help=(
            'Stringency for how close the playlist dureation should be tp the '
            'specified time limit (does not guarantee stringency).'
        ),
        required=False,
        type=int,
    )

    return parser


def convert_minutes(duration):
    minutes = int(duration)
    seconds = duration - minutes
    seconds = int(seconds * 60)
    return minutes, seconds


if __name__ == '__main__':
    main()
