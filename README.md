# Drone-show-by-using-crazyflie
This is tips for making drone show with crazeflie2.1 of [bitcraze](https://www.bitcraze.io/)

![10drones](https://user-images.githubusercontent.com/72853382/131221009-4494291d-d2ac-4419-80f0-05a0770282fa.gif)
![시퀀스 01_2](https://user-images.githubusercontent.com/72853382/131221187-f9d89928-0388-43f2-b68e-ff6810ca7fff.gif)   
5 drones fly with drawing '30',    
   
![11drones](https://user-images.githubusercontent.com/72853382/131221011-c22d4222-7309-43c9-bffe-75233a641ac3.gif)   
11 drones fly with led light
   
umm... gif quality is bad 
   
# 0. short story
<details><summary>[click to see]</summary>
  
  ~~~
  From now on, still the key application of drone is led drone show
  And the key points of the drone show are high accurate positioning and nice trajectory design   
     
  For accurate positioning, there are RTK GPS for big scale and outdoor drone show, motion capture system for indoor drone show
  In my case, I gonna use crazyflie2.1, the micro drone which is under 30g and 15cm size, and lighthouse positioning system
    
  Actually the positining system is not my work, cause already bitcraze have done
  Then, my work is make a nice trajectories, and usually it's very time spanding task
  I searched some stuffs and found [this](https://droneshowsoftware.com/)
  The Drone Show Software mayb the modified version of blender which is opensource 3d desing tool
  So, I tried to make drone show trajectory with blender and I gonna share the stuff and tips
  ~~~
</details>

# 1. blender
<details><summary>[click to see]</summary>
  
  
  (1) Download a [blender](https://www.blender.org/)   
     
     
  (2) Learn basic control of blender with youtube tutorial, there are lots of blender tutorial for beginners   
      At least, we need to know how to move objects in 3d space
  
</details>

# 2. blender script
<details><summary>[click to see]</summary>
  
  
  (1) move to Scripting tab and click run scripts
   ![Screenshot from 2021-08-29 00-46-08](https://user-images.githubusercontent.com/72853382/131223382-bef40993-e940-45d8-9a9f-ad7ce78c2765.png)
   ![Screenshot from 2021-08-29 00-46-23](https://user-images.githubusercontent.com/72853382/131223387-6aff5ca5-b86a-4605-a758-bda07e8e9bc0.png)


  
</details>

# 3. python file
<details><summary>[click to see]</summary>
  (1) explanation of the file   
   
   >   
   I modified the [example pythone file of bitcraze](https://github.com/bitcraze/crazyflie-lib-python/blob/master/examples/swarm/synchronizedSequence.py)   
   So, we need to know the original example file simply   
   The modified file is [drone_show.py](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py)   
    
   important parts of the modified file       
  > a. [STEP_TIME](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L53)   
  > b. [uris](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L64-L79)   
  > c. [sequence array](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L86-L110)   
  > d. [key input](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L229-L236)   
   
      
      
   (2) edit the python file   
      
 example [drone_show_example_11drone.py](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show_example_11drone.py) is the file of the 11 drones   
      fly with led light which is the third gif on readme   
     
   
  > a. [STEP_TIME](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L53) : 1 means 1fps, 0.5 means 2fps, 0.333 means 3fps ...      
  > b. [uris](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L64-L79)   
  > c. [sequence array](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L86-L110)  : add the sequence frome the file that made by blender python script    
  > d. [key input](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show.py#L229-L236)  : matching key_input and sequence      
   
   </details>
   
   
   # 4. run 
   <details><summary>[click to see]</summary>
   
 >  If you using many drones, then it takes few time to initialize   
>   So, you need to wait until every crazyflie's led ring take off   
 >    
>   [drone_show_example_11drone.py](https://github.com/beomsu7/Drone-show-by-using-crazyflie/blob/main/drone_show_example_11drone.py) is the file of the 11 drones >fly with led light which is the third gif on readme   
 >  I entered the following key_input in sequence 'takeoff', 'start', 'dance', 'end', 'land'   
      
    $ python3 drone_show_example_11drone.py   
    $ # wait until every crazyflie's led ring take off   
    $ takeoff # 11 drones takeoff   
    $ start # 11 drones move to initial position of sequence   
    $ dance   
    $ end # 11 drones go back to initial position   
    $ land # 11 drones land   
   
  
</details>
