# Import the TV class from the tv.py
# Create 2 TV objects
# Make the first TV object turn on and set the channel to 30 and volume to 3
# Make the second TV object turn on and set the channel to 3 and volume to 2

from tv import TV

def main():
    tv1 = TV()
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume(3)

    tv2 = TV()
    tv2.turn_on()
    tv2.set_channel(3)
    tv2.set_volume(2)

    # Display the channel and volume for both tv1 and tv2
    print(f"tv1's channel is {tv1.get_channel()} and volume is {tv1.get_volume()}")
    print(f"tv2's channel is {tv2.get_channel()} and volume is {tv2.get_volume()}")

    # Adjust the channel and volume for both tv1 and tv2 
    tv1.channel_up()
    tv1.volume_up()
    print(f"tv1's channel is {tv1.get_channel()} and volume is {tv1.get_volume()}")

    # Adjust the channel and volume for both tv1 and tv2
    tv2.channel_down()
    tv2.volume_down()
    print(f"tv2's channel is {tv2.get_channel()} and volume is {tv2.get_volume()}")

    # Turn off tv1 and tv2
    tv1.turn_off()
    tv2.turn_off()
    print(f"tv1 is {tv1.get_state()}")
    print(f"tv2 is {tv2.get_state()}")

    # Try to set the channel and volume for tv1 and tv2 when they are off
    tv1.set_channel(50)
    tv1.set_volume(5)
    tv2.set_channel(5)
    tv2.set_volume(4)
    print(f"tv1's channel is {tv1.get_channel()} and volume is {tv1.get_volume()}")

if __name__ == "__main__":
    main()
