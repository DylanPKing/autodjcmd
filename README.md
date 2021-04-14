# FYP CMD Client

This is a command-line client for my Final Year Project.

## Setup

1. Create a virtual environment.
```bash
python -m venv .env
```

2. Load the newly created virtual environment.
    - Linux
    ```bash
    source .env/bin/activate
    ```

    - Windows
    ```
    .env/Scripts/activate
    ```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running
```bash
python autodjcmd [--params-here] --total-duration [int here] 
```


To run the program, you need to specify parameters that the server must adhere to.

### Arguments
```
usage:  [-h] [--original-artist ORIGINAL_ARTIST] [--year YEAR] [--position POSITION]
        [--keyword {river,love,blues,party,time,tonight,rain,morning,breathe,fire,woman,disco,rock,music,dancin,baby,twist,lonely,stop,boogie,christmas,moon}] [--total-duration TOTAL_DURATION]
        [--include-tracks-at INCLUDE_TRACKS_AT] [--tolerance-window TOLERANCE_WINDOW]

optional arguments:
  -h, --help            show this help message and exit
  --original-artist ORIGINAL_ARTIST
                        Search for tracks with the same original artist
  --year YEAR           Search for tracks released in the same year.
  --position POSITION   Search for tracks with the same track number.
  --keyword {river,love,blues,party,time,tonight,rain,morning,breathe,fire,woman,disco,rock,music,dancin,baby,twist,lonely,stop,boogie,christmas,moon}
                        Search for tracks with a specified keyword in the title.
  --total-duration TOTAL_DURATION
                        The length of the playlist you would like to generate.
  --include-tracks-at INCLUDE_TRACKS_AT
                        Path to a JSON file containing tracks you would like to be included.
  --tolerance-window TOLERANCE_WINDOW
                        Stringency for how close the playlist duration should be to the specified time limit (does not guarantee stringency).
```

