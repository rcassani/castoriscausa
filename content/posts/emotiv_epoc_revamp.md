Title: Revamping Emotiv Epoc
Date: 2017-09-16 19:00
Category: Projects
Tags: EEG, DIY, hack
Slug: emotive-epoc-hack
Author: Raymundo Cassani
Thumbnail: final_box.jpg

The [**Emotiv Epoc**](https://www.emotiv.com/epoc/) is a 14-channel EEG headset that brought the concept of affordable wireless EEG to the general public, paving the road for later portable EEG systems. It has been used for in [several studies](https://www.emotiv.com/category/independent-studies/).

Unfortunately, the **Epoc** presents two characteristics that make some experiments unpractical. **(1) The electrode placement**, fix as it is,  forbids locating electrodes on some interesting scalp places for certain EEG, for example on the central line. **(2) The technology of the electrodes**, the contact between the electrode and scalp is mediated by sponges that need to be wet with saline solution, thus for long recordings (>1 hr), the solution starts to dry affecting the quality of the EEG signals.

After some years of use at our laboratory, the [**MuSAE Lab**](http://musaelab.ca/), the structure that holds the **Epoc** arms as one piece got broken. While this condition could be fixed, we opted to follow the approach taken by Stefan Debener in the 2012 paper [*How about taking a low-cost, small, and wireless EEG for a walk?*](https://www.researchgate.net/profile/Stefan_Debener/publication/231212716_How_about_Taking_a_Low-Cost_Small_and_Wireless_EEG_for_a_Walk/links/0046352a9c6332593a000000/How-about-Taking-a-Low-Cost-Small-and-Wireless-EEG-for-a-Walk.pdf), this is to say, to remove the electronics from the EEG headset and give it a new (and more practical) case.

<center>
[<img src="/images/epoc_broken.png" style="width: 500px;">](/images/epoc_broken.png)
Emotiv Epoc. In the red the part that was broken.
</center>  

Beside the new casing:

1. The original battery was replaced by a [3.7V @ 1100mAh battery](https://www.aliexpress.com/item/best-battery-brand-3-7V-403759-1100mAh-Lithium-Polymer-Li-Po-Rechargeable-DIY-Battery-For-Mp3/32811781166.html?spm=2114.search0305.4.72.jsEKtf), with a size 4 x 37 x 59 mm (important to the case design).
2. The EEG headset cables were replaced by [cables ended in the DIN (touch-proof) connectors](https://shop.openbci.com/collections/frontpage/products/touch-proof-electrode-cable-adapter?variant=31007211715) to support different standard electrode models.

| [<img src="/images/battery_epoc_vamping.jpeg" style="width: 500px;"/>](/images/battery_epoc_vamping.jpeg)| <img src="/images/square_500_clear.png" style="width: 100px;"/> |[<img src="/images/cables_epoc_vamping.jpg" style="width: 380px;"/>](/images/cables_epoc_vamping.jpg)   |
|:-:|:-:|:-:|
|[3.7V 1100mAh battery](https://www.aliexpress.com/item/best-battery-brand-3-7V-403759-1100mAh-Lithium-Polymer-Li-Po-Rechargeable-DIY-Battery-For-Mp3/32811781166.html?spm=2114.search0305.4.72.jsEKtf)|    | [EEG DIN (touch-proof) cables](https://shop.openbci.com/collections/frontpage/products/touch-proof-electrode-cable-adapter?variant=31007211715)|

<br>
The vamping process consisted of four parts:

1. Striping the electronics from the **Epoc**
2. Soldering the new battery and electrode cables
3. Placing everything in the new case

### 1. Striping the electronics
This part was performed by [Liviu Ivanescu](http://musaelab.ca/our-team/), here some of the pictures.

| [<img src="/images/IMG_7474.JPG" style="width: 500px;"/>](/images/IMG_7474.JPG)   | <img src="/images/square_500_clear.png" style="width: 100px;"/>| [<img src="/images/IMG_7501.JPG" style="width: 500px;"/>](/images/IMG_7501.JPG) |
|:-:| |:-:|
| [<img src="/images/IMG_7563.JPG" style="width: 500px;"/>](/images/IMG_7563.JPG) | <img src="/images/square_500_clear.png" style="width: 100px;"/>| Additional photos on the Epoc interior can be found [here](https://www.flickr.com/photos/43372242@N06/with/3993993098/) and in this [report](https://fccid.io/document.php?id=1274219). |
<br>

### 2. Replacing the battery and electrode cables
The soldering part is the most crucial, as screwing it screws the EEG device that was working (however it was not useful with the broken structure). Note that thru-hole pads for the cables interconnect the top and bottom layer of the PCB, i.e. they are [Thru-hole Vias](https://en.wikipedia.org/wiki/Via_(electronics)), thus it is not needed to pass the cables through the hole, a surface soldering will be enough to assure a good electric contact.

<center>
[<img src="/images/thru_hole_solder.jpg" style="width: 500px;"/>](/images/thru_hole_solder.jpg)  
Surface soldering.
</center>  

### 3. Place everything in a new casing
The approach for the case was 3D printing, the models was designed in [Tinkercad](https://www.tinkercad.com) as publicly available [here](https://www.tinkercad.com/things/32Eoo5m7Skp-epoch-box). It 3D printed at [District3](http://d3center.ca/en/home/).

| [<img src="/images/tinker_image.png" style="width: 500px;"/>](/images/tinker_image.png)| <img src="/images/square_500_clear.png" style="width: 100px;"/> |[<img src="/images/placement_box.jpg" style="width: 380px;"/>](/images/placement_box.jpg)   |
|:-:| |:-:|
|[Tinkercad model](https://www.tinkercad.com/things/32Eoo5m7Skp-epoch-box)| |Placement of components|

<center>
[<img src="/images/final_box.jpg" style="width: 600px;"/>](/images/final_box.jpg)  
Final result, a Canadian looney ($1) with a 26.5 mm diameter as reference.
</center>

<br>
To keep the the elements in its place I used segments of silicone bars, which happened to be very useful for that purpose. To take the cables out of the box, a [rubber wiring grommet](https://www.waytekwire.com/products/1398/Grommets/) was used.

Finally a quick road test, **Epoc** in its new case + a bucket of salt water + ECG signal.
<center>
[<img src="/images/testing_epoc.jpg" style="width: 500px;"/>](/images/testing_epoc.jpg)  
</center>


### Conclusion
The hole process of tuning up the **Epoc** was a great experience, and I hope this post can help others in repairing and / or improving their own **Epoc** devices.
