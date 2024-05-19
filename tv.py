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

    # Get the current state of the TV
    def get_state(self) -> bool:
        return "on" if self.on else "off"

    # Get the current channel
    def get_channel(self) -> int:
        if not self.on:
            print("TV is off")
            return None
        return self.channel
    
    # Set the channel
    def set_channel(self, channel: int) -> None:

        # Check if TV is on and channel is between 1 and 120
        if not self.on:
            print("TV is off, cannot set channel")
            return
        if 1 <= channel <= 120:
            self.channel = channel
        else:
            print("Invalid channel number")


    # Get the current volume
    def get_volume(self) -> int:
        if not self.on:
            print("TV is off")
            return None
        return self.volume
    
    # Set the volume
    def set_volume(self, volume: int) -> None:

        # Check if TV is on and volume is between 1 and 7
        if not self.on:
            print("TV is off, cannot set volume")
            return
        if 1 <= volume <= 7:
            self.volume = volume
        else:
            print("Invalid volume level")

    # Channel up
    def channel_up(self) -> None:
            
        # Check if TV is on and channel is less than 120
        if not self.on:
            print("TV is off, cannot change channel")
            return
        if self.channel < 120:
            self.channel += 1
        else:
            print("Channel is already at maximum")

    # Channel down
    def channel_down(self) -> None:
        
        # Check if TV is on and channel is greater than 1
        if not self.on:
            print("TV is off, cannot change channel")
            return
        if self.channel > 1:
            self.channel -= 1
          
        else:
            print("Channel is already at minimum")
    # Volume up
    def volume_up(self) -> None:

        # Check if TV is on and volume is less than 7
        if not self.on:
            print("TV is off, cannot change volume")
            return
        if self.volume < 7:
            self.volume += 1
        else:
            print("Volume is already at maximum")
    
    # Volume down
    def volume_down(self) -> None:

        # Check if TV is on and volume is greater than 1
        if not self.on:
            print("TV is off, cannot change volume")
            return
        if self.volume > 1:
            self.volume -= 1
        else:
            print("Volume is already at minimum")