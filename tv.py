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

    # Turn on the TV
    def turn_on(self) -> None:
        self.on = True

    # Turn off the TV
    def turn_off(self) -> None:
        self.on = False

    # Get the current channel
    def get_channel(self) -> int:
        return self.channel
    
    # Set the channel
    def set_channel(self, channel: int) -> None:

        # Check if TV is on and channel is between 1 and 120
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    # Get the current volume
    def get_volume(self) -> int:
        return self.volume
    
    # Set the volume
    def set_volume(self, volume: int) -> None:

        # Check if TV is on and volume is between 1 and 7
        if self.on and 1 <= volume <= 7:
            self.volume = volume

    # Channel up
    def channel_up(self) -> None:
            
        # Check if TV is on and channel is less than 120
        self.channel = self.channel + 1 if self.on and self.channel < 120 else self.channel

    # Channel down
    def channel_down(self) -> None:
        
        # Check if TV is on and channel is greater than 1
        self.channel = self.channel - 1 if self.on and self.channel > 1 else self.channel