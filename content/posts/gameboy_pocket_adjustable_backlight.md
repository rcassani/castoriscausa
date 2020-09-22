Title: Game Boy Pocket with adjustable backlight
Date: 2020-09-20 21:34
Tags: DIY, hack, Game Boy
Author: Raymundo Cassani
Slug: gameboy-pocket-adjustable-backlight
Thumbnail: gbp_1st.jpg

Some months ago I got the this [LED panel](https://handheldlegend.com/collections/game-boy-pocket-mgb/products/game-boy-backlight-v3) from [Hand-Held Legend](https://handheldlegend.com/) to add backlight to the display of the [Game Boy Pocket](https://en.wikipedia.org/wiki/Game_Boy_family#Game_Boy_Pocket). The installation was quite simple and went without problems using the [instructions](https://handheldlegend.com/collections/game-boy-pocket-mgb/products/game-boy-backlight-v3) provided and this useful [video](https://youtu.be/i0PlML-q4Lo). As the panel is powered is connected to 5 V, a resistor of 100 or 150 $\Omega$ is required to avoid a super bright backlight.

<center>
[<img src="/images/gbp_1st.jpg" style="width: 300px;">](/images/gbp_1st.jpg)<br>
Game Boy Pocket with backlight.<br>
</center>

Last weekend, I revisited my modded Game Boy and realized that I haven't used it as much as I expected.

**The culprit?**, the backlight itself, the intensity is good during daytime, but it's too bright to play at night in a dim room. To fix this, I decided to install a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer) and make it easily accessible to change the backlight intensity accordingly. This modification was a success and I am very satisfied with the [result](#result). Below I describe the procedure for modding the Game Boy Pocket.

## Procedure
### Materials
To install the LED backlight panel adjustable backlight, check the [Required Equipment](https://handheldlegend.com/collections/game-boy-pocket-mgb/products/game-boy-backlight-v3). For the wiring I used [magnet wire](https://en.wikipedia.org/wiki/Magnet_wire) 28 AWG, as it's easy to hide and pass through tight places. Also, sandpaper, a drill and drill bits are needed, this is be cause to add the potentiometer two extra modifications are needed:

1. Enlarging an existent hole in the PCB with a 3/64" or 1/16" drill bit.

2. Making a new hole in the plastic case with a 1/8" drill bit.

Beside the panel, a 100 $\Omega$ resistor and 5 k$\Omega$ potentiometer are needed. Due to the space limitations, I used as vertical skeleton trimmer potentiometer or [trimpot](https://en.wikipedia.org/wiki/Trimmer_(electronics)#Resistors).

<center>
[<img src="/images/gbp_sv_trimpot.jpg" style="width: 300px;">](/images/gbp_sv_trimpot.jpg)<br>
Skeleton vertical trimpot.<br>
</center>

### Installation
The electronic components: LED panel (D1). 100 $\Omega$ resistor (R1) and the variable resistor (R2) are connected as follows.

<center>
[<img src="/images/gbp_circuit.png" style="width: 600px;">](/images/gbp_circuit.png)<br>
Electric circuit for adjustable backlight.<br>
</center>

The fact that R1 and R2 are "before" and "after" the D1 does not matter, the y could be in any place in the series circuit. However, they were placed like that to facilitate the physical installation of the components. The installation can be broken in three parts:

1. LED panel placement  
2. Connection to 5 V  
2. Trimpot placement and connection to ground  

### 1. LED panel placement  
For this first part, follow the instructions in this video:

<center>
[<img src="/images/gbp_youtube.png" style="width: 600px;">](https://youtu.be/i0PlML-q4Lo){:target="_blank"}
</center>

### 2. Connection to 5 V
The positive connection of the LED panel is done through R1, and can be done to this point.

<center>
[<img src="/images/gbp_pos.jpg" style="width: 600px;">](/images/gbp_pos.jpg)<br>
Connection to 5 V.<br>
</center>

### 3. Trimpot placement and connection to ground
Let's prepare the trimpot. Remove the pins for the both the extreme connections. And by seen the trimpot from the back, place a drop of solder in the right connection.

<center>
[<img src="/images/gbp_trimpot.jpg" style="width: 600px;">](/images/gbp_trimpot.jpg)<br>
Preparing the trimpot.<br>
</center>

Enlarge this existing [through hole](https://en.wikipedia.org/wiki/Through-hole_technology) in the PCB with the 3/64" drill bit. This through hole connects two ground planes on each side of the PCB.

<center>
[<img src="/images/gbp_drill.jpg" style="width: 600px;">](/images/gbp_drill.jpg)<br>
Through hole to enlarge.<br>
</center>

With help of sandpaper and patience remove the paint around the new through hole on both sizes of the PCB and insert the trimpot facing back, with the position it will fit nicely in the case.

<center>
[<img src="/images/gbp_solder.jpg" style="width: 400px;">](/images/gbp_solder.jpg)<br>
Placing trimpot.<br>
</center>

Solder the negative connection of the LED panel to the trimpot terminal that has already solder.

<center>
[<img src="/images/gbp_neg.jpg" style="width: 600px;">](/images/gbp_neg.jpg)<br>
Connection to graound.<br>
</center>

Finally, close the Game Boy Pocket and identify where the trimmer is make hole with the 1/16" drill bit in the case. In my case, I have a clear case, which makes the task way more easier.

<center>
[<img src="/images/gbp_case.jpg" style="width: 400px;">](/images/gbp_case.jpg)<br>
Game Boy Pocket case with hole<br>
</center>

Close the Game Boy and enjoy the adjustable backlight.

## Result
<center>
[<img src="/images/gbp_adj_result.gif" style="width: 400px;">](/images/gbp_adj_result.gif)<br>
Game Boy Pocket with adjustable backlight.<br>
</center>

For the moment, I need a small flat screwdriver to adjust the backlight intensity. I have in mind to 3D print a small piece to do adjustment, something like a watch crown.
