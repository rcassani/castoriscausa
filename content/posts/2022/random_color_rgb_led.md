Title: Random color RGB LED
Date: 2022-07-02 13:57
Tags: DIY, Python, electronics
Author: Raymundo Cassani
Slug: random_color_rgb_led
Thumbnail: amiks.png

Often, there is the need of generating a random [RGB color for LEDs](https://en.wikipedia.org/wiki/Light-emitting_diode#RGB_systems). The most common approach is to obtain a random value between 0 and 1 (or 0 and 255) for the **Red**, **Green** and **Blue** channels.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d6/RGB_color_cube.svg" style="width: 90%;"/>  
RGB cube
</center>

This approach, however, leads to dark and light colors which may not be goal when picking a random color for a RGB LED, **we want color!**

As such, an alternative is to pick a color in the [HSV space](https://en.wikipedia.org/wiki/HSL_and_HSV#Basic_principle), more specifically in the circle at the top of the HSV cone (`value=1`). While this avoids dark colors, there is a large probability of getting light (pastel) colors. Thus the search for random colors can be constrained to be nearby the rim of such circle, this is to say saturation cannot be smaller than 0.8.

<center>
[<img src="/images/hsv_spaces.png" style="width: 90%;"/>](/images/hsv_spaces.png)  
Circle at the top of the HSV cone (`value=1`). Left, `saturation=[0, 1)`. Right, `saturation=[0.8, 1)`.
</center>

Lastly, this Python scripts shows the results of picking **625 colors** from the RGB space (left) and the outer rim of the `value=1` HSV circle (right).

<center>
[<img src="/images/random_color_comparison.png" style="width: 90%;"/>](/images/random_color_comparison.png)  
Picking random colors from the RGB space (left) and the outer rim of top of the HSV cone (right).
</center>

    python
    {!> https://gist.githubusercontent.com/rcassani/f7ef73868b903eeb4370febfaf0cafb8/raw/5dc4a3c929cff11826704f5cb2afe37e4a58899c/random_colors.py !}
