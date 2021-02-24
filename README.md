# Artemia Feeder: Advancing the Design for Fish Larvaeculture

## Background:
Our sponsor, an aquaculture researcher, needed an updated graphical user interface to accurately and automatically feed his supply of striped bass larvae. Our design improved upon the design of a previous senior design team’s user interface by making it easier to control their pump-based feeding system without jumping through numerous hoops, such as running the original LiveFeeder (a program that initiates the feeding system) through a series of command line prompts in Terminal. The GUI, written in Python, incorporates graphs and sliders in its design in order to display the information of past feedings, while also enhancing the user-friendliness of the design.


<p align="center">
  <img src="https://i.imgur.com/8LKCdiW.png" width="579" height="434" />
</p>


## Design Highlights

### Graphical User Interface

The initial interface so that rather than a series of command-line prompts, the user can easily manipulate the desired artemia concentrations, liquid volumes in cones, feeding rate, start delay, number of feeding cycles, and feeding intervals using color-coded sliders and drop-down menus. 

(photo of what that's describing goes here)

This interface also has the capability of plotting previous feedings to a graph. The number of recent feedings to be plotted can be selected from 5, 10, or 20 and the GUI will produce the desired graph accordingly.

(photo of what that's describing goes here)


### LiveFeeder 2.0

LiveFeeder is the name of the program used to run the pump-based feeding system. This program was updated so that it can be implemented with our GUI. The changes in the source code allow for files produced by the interface (which contained sets of numbers corresponding to selected inputs) to be read so that the values contained within those files are written to variables defined in LiveFeeder. The feeding pumps will then run using these values.

(show photo of livefeeder)


### Concentration Checker (de-scoped)

(describe how this would have operated, then post schematic)


## Demo

(an unlisted youtube link will go here)


