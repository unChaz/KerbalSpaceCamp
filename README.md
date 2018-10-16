# Kerbal Space Camp
There was once an ambitious idea to make the video game Kerbal Space Program into a multiplayer in-person experience. This application was built to do just that. This program runs multiple versions of Kerbal Space Program and syncs them up over a LAN. The master instance of the game can do anything, whereas the slave can only view and create Maneuver nodes. The master instance runs on the machine that acts as the capsule, and the slave is the terminal of mission control. At the same time a web server runs displaying information on the mission such as velocity, fuel consumption, etc.

We found that for the best experience lock the "pilot" in a washing machine box with a headset and a joystick. To achieve realistic simulation a 3rd party must occasionally shake the box while the "ship" is performing a maneuver. 

## Dependencies
- Python 2.7.9

## Getting Started
1) You will need to purchase your own distribution of Kerbal Space Program.

2) Copy your KSP directory contents into the KerbalSpaceCamp directory.

3) Run the install.py script under scripts.
