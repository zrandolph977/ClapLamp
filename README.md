# ClapLamp

This repository will be home to the code that allows us to turn a lamp on or off using the power of claps.


## Release Notes



## Setup

## Required materials

Items required for this project include:
<ul>
    <li>Raspberry Pi</li>
    <li>5 Volt Relay</li>
    <li>USB microphone</li>
    <li>Lamp</li>
</ul>

Pinout:
<ul>
    <li>Use Pin 12 for data connection to the relay.</li>
    <li>Use any 5V pin and any ground pin.</li>
    <li>Since we're using Pyaudio it automatically will pickup any usb microphone.</li>
</ul>



### Final Commit 11/27/2022

    Final commit includes threads to continually check the amount of claps. Using this you can assign different actions based on the amount of claps.
# Updates
Finished product uses pyaudio library to read bytestream looking for certain pitches for claps.

Milestone Breakdown:

M1: Started figuring out what we wanted to do in the first place. We had decided to try making a discord bot but decided we didn't really know WHAT we wanted to bot to do. Then we decided on the clap lamp...

M2: Implementation started on the lamp, at this stage we had the lamp wired up to the raspberry pi, the relay, and were able to run it with a button.

M3: At this point, we pretty much had the lamp working. Saebastion was in cahrge of the implementation and was able to work his way through it on his own. There were still some kinks at this point though with figuring out a good audio range to listen for so the lamp could be triggered from clapping but not talking.

Final Milestone: At this point, we had the lamp dialed in. We were able to talk aroud it without the lamp turning on or off and have it ONLY be triggered by claps (or some other really loud noise like screams or something). Essentailly, the microphone is constantly listening for a sudden increase in amplitutde in rapid succession and will trigger the relay when it hears two claps. It does sometimes go off if you're laughing really loud because the mic picks it up and it's pretty much impossible to tell the difference from a clap when all we're checing for is a rapid change in sound amplitude.

