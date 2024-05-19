# Create class TV and define state variables
# Define methods: turn on/off, get channel, set channel
# get volume, set volume, channel up, channel down
# volume up, volume down

class TV:

    # Initialize state variables and their types
    def __init__(self) -> None:
        self.channel: int = 1
        self.volume: int = 1
        self.on: bool = False