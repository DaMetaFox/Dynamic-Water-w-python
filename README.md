
<h1>
  <p align="center">
    Dynamic Water whit python
  </p>
</h1>

<br>

<!--introduction--------------------------------------------------------------------------------------------------------------------------------------------->
<h2>
  <p align="center">
    A brief introduction
  </p>
</h2>

<p> The easyiest way to design dynamic water is to create a string of indevidual "springs". In each frame a springs height update is done based on Hooke's law.
    Is also need a loss funtion to decrease the energy of the system and a spread constant that regulates how much energy passes from a spring to the neigbors.
</p>

  ```
    K = Spring strength
    D = Energy loss
    SPREAD = energy spread
    SPRING SEPARATION = distance between springs (px)
  ```
  
  
<br>
<br>
<br>


<!--examples------------------------------------------------------------------------------------------------------------------------------------------------>
<h2>
  <p align="center">
     Here you have a few explanations/tutorials:
  </p>
</h2>

<br>



<!-- first video -->
<h3>
  <p align="center">
     2D Dynamic Water Tutorial by HackTrout
  </p>
</h3>

<h3 align="center">
  
  [![2D Dynamic Water Tutorial by HackTrout](https://img.youtube.com/vi/2UlWRWVszWs/0.jpg)](http://www.youtube.com/watch?v=2UlWRWVszWs)
<h3>

  <!-- secon video-->
 
<br>
<br>
<br>
  
<h3>
  <p align="center">
     How to Make Water with Dynamic Waves by Pixelipy
  </p>
</h3>

  
<h3 align="center">
  
  [![2D Dynamic Water Tutorial by HackTrout](https://img.youtube.com/vi/RXIRkou021U/0.jpg)](http://www.youtube.com/watch?v=RXIRkou021U)
<h3>
  
  <!-- the simulation-->
<br>
<br>
<br>
  
<h3>
  <p align="center">
     Godot Water 2D Simulation by pixelipy
  </p>
</h3>

  
<h3 align="center">
 
  
<h3>
<p align="center">
  <a href=https://pixelipy.itch.io/water-2d-simulation>
    <img width="500" src=https://github.com/DaMetaFox/Image_cloud/blob/main/Dynamic_Water_godot_simulation.png>
  </a>
</p>
  
  
<!-- Usage examples---------------------------------------------------------------------------------------------------------------------------------------->
<br>
<br>
<br>
<br>
  
<h2>
  <p align="center">
    Usage examples:
  </p>
</h2>

  
>__Warning__ 
> <p> Make sure you have both python3 and pygame installed </p>

  

<!--rock_test.py----------------------------------------------------------------------------------------------------------------------------------------->
  
<br>
<br>
<br>

  <h3>
    <p>
      Raining rocks
    </p>
  </h3>

<br>

In the first example `rock_test.py`, whenever you press the mouse, a rock should fall. In each update we use `WaterBody.is_on_shallow()` to check if the rock is on the white line of the water, if true `WaterBody.splash()` is called, creating a splash. Don't forget to call `WaterBody.update()` in each frame.

  
<!--square_test.py----------------------------------------------------------------------------------------------------------------------------------------->
<br>
<br>
<br>
  <h3>
    <p>
      Square pet
    </p>
  </h3>
<br>

In the second example `square_test.py`, a square will follow your mouse. In each frame the square will rotate and move towards the mouse using the vectors. We check if the square is touching in the white line of the water whit `WaterBody.is_on_shallow()`, if it is we create a perturbation based on the `y` velocity of the square. `WaterBody.update()` is obviously called.

  
<!-- Documentation--------------------------------------------------------------------------------------------------------------------------------------->
<br>
<br>
<br>

<h2>
  <p align="center">
    Documentation
  </p>
</h2>

<!--Splash------------------------------------------------------------------------------------------------------------------------------------------------>
<br>
<br>

> <h3>WaterBody</h3>
>
>
>          WaterBody(window, topleft_x, topleft_y, width, height) --> None:
>               window -->   a display window ... pygame.Surface()
>               topleft_x --> the topleft x position of the water on the given surface
>               topleft_y --> the topleft y position of the water on the given surface
>               width -->   the width of the WaterBody
>               heigth -->   the heigth of the WaterBody
>
>            optional:
>               K = 0.0045
>               D = 0.0050
>               SPREAD = 0.038
>               SPRING_SEPARATION = 4
>               COLOR = [40, 53, 255]
>               ALPHA = 60
>               
><br>
> &nbsp;&nbsp;&nbsp;Creates a new instance of WaterBody. 


<!-- Funtions-------------------------------------------------------------------------------------------------------------------------------------------->
<h3>
  <p>
    Functions:
  </p>
</h3>
<!--Splash------------------------------------------------------------------------------------------------------------------------------------------------>
<br>
<br>

> <h3>splash</h3>
>
>
>          WaterBody.splash(center_x, width, force) --> None:
>               center_x -->   the center of the splash
>               width -->   how many pixels should be pulled
>               force -->   an integer positive or negative that represents how many pixels should each spring is pulled
>
><br>
> &nbsp;&nbsp;&nbsp;Creates a splash on the water by pulling n springs with a given force


<!--is_on_water------------------------------------------------------------------------------------------------------------------------------------------------>
  <br>
  <br>
  <br>
  
>  <h3>is_on_water</h4>
>  
>            
>           WaterBody.is_on_water(mask, topleft_x, topleft_y) --> Boolean:
>               mask -->   a pygame.mask.Mask() object
>               topleft_x -->   the mask's topleft x position
>               topleft_y -->   the mask's topleft y position
>  
> <br> 
> &nbsp;&nbsp;&nbsp;Returns True if the given mask is touching on the water



<!--is_on_shallow------------------------------------------------------------------------------------------------------------------------------------------------>
  <br>
  <br>
  <br>
  
>  <h3>is_on_shallow</h4>
>  
>            
>           WaterBody.is_on_shallow(mask, topleft_x, topleft_y) --> Boolean:
>               mask -->   a pygame.mask.Mask() object
>               topleft_x -->   the mask's topleft x position
>               topleft_y -->   the mask's topleft y position
>  
> <br> 
> &nbsp;&nbsp;&nbsp;Returns True if the given mask is touching on the white line of the water
  
  
  
  
  
<br>
<br>
<br>
<br>


<!--Variables & Stuffs-------------------------------------------------------------------------------------------------------------------------------------------->
<h3>
  <p>
    Variables & Stuffs:
  </p>
</h3>

> <h4>
>  
> `WaterBody.topleft_x` and `WaterBody.topleft_y` vs. `Waterbody.mask_topleft_x` and `WaterBody.mask_topleft_y`
>
> </h4>
>
>    
>&nbsp;&nbsp;&nbsp;&nbsp;  **topleft_x** and **toplfet_y** represent the topleft coordinates of the visible water, but since the water is waveling, `WaterBody.surface` is 3 times bigger than the visible heigth. So WaterBody.mask_topleft_y represents the true _y_ of `WaterBody.surface` on the given `window`.
>
    
  
<br>
<br>
<br>
<br>

<!--any doubt?------------------------------------------------------------------------------------------------------------------------------------------------->
<h3> If you have any questions text me </h3>

<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Discord ????&nbsp;
   <a href="https://discord.gg/hXyhbs6Arh">
    <img align = "center" src="https://github.com/DaMetaFox/DaMetaFox/blob/main/pictures/_icon_discord.png" width="35"/>
  </a>
</p>

<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Gmail ????&nbsp;
   <a href="mailto:pedroxavierfigueira2008@gmail.com">
    <img align = "center" src="https://github.com/DaMetaFox/DaMetaFox/blob/main/pictures/_icon_gmail.png" width="40"/>
  </a>
</p>
<br>


> __Warning__
> <h5>I rarely see my gmail</h5>

<br>
<br>
<br>
  
<!--About me--------------------------------------------------------------------------------------------------------------------------------------------------->
<h5> If you want to know more about me you can read my 
  <a href = "https://github.com/DaMetaFox/DaMetaFox/blob/main/README.md">
  github profile
  </a>
</h5>

  
  
<h5> This is hard work, please consider a donation: I'm hungry
  <a href = "https://github.com/DaMetaFox/DaMetaFox/blob/main/pictures/paypal_qrcode.jpg">
    <img align="center" width="80" src="https://github.com/DaMetaFox/DaMetaFox/blob/main/pictures/_icon_paypal.png">
  </a>
</h5>
