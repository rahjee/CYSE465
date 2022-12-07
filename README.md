# CYSE465
I initially thought of the attack as having multiple cars utilizing LiDAR-based technology in the same area, which would cause some vehicles' LiDAR sensors to not function properly. After doing so, David and I fully configured LGSVL; here, we faced many issues that David was able to solve, as he will mention in his section. Before David solved some of the problems met, I spoke with ORC directly for an hour to discuss solutions to some of the problems. The issues included being unable to run LGSVL as exouser and as root. I could also not run LGSVL in both instances made available to us, the Graphical Desktop and the GPU Accelerated Desktop. I faced a “segmentation fault (core dumped)” error in the GPU Accelerated Desktop instance whenever I attempted to start LGSVL. We did not end up meeting that issue in the Graphical Desktop which led David and me to go that route. I researched possible attack methods and found a wide variety of resources on the internet. I used these resources to get a vehicle to function with our user control via keyboard and included a LiDAR-based sensor on the car.
Once I got LGSVL functional, I started getting Velodyne, a method of grabbing LiDAR data. David was able to get up to 16 LiDAR lasers active with Velodyne and captured some random data points; however, we could not correctly link Velodyne’s sensors to our vehicle in LGSVL, even by using the help guide. 
I then moved to install ROS and ROS2 to complete some more testing of LiDAR data grabbing, yet unsuccessful. I had to install specific modules such as nodejs and LGSVL_msgs. With these modules, I could view the LiDAR data linked from LGSVL in a program called RViz. After countless hours of troubleshooting and testing, I, with the help of David, was able to visualize the LiDAR data from a vehicle in LGSVL. I recorded all of the RViz setups we underwent, which totaled roughly 6-8 hours of footage, to help us troubleshoot issues in the future. Other problems include random files corrupting, forcing me to remove and re-install them. We even emailed you some of the specific issues we faced. I eventually got RViz working which was a game changer as now we could visualize the LiDAR data in real time. I then configured a new simulation in LGSVL called “FINAL TEST3” which was used in the demo. I knew that only one vehicle could be bridged to RViz, which was fine as we only needed to visualize the data for one vehicle to test if other LiDAR sensors would cause a malfunction in the primary car’s LiDAR sensors. 
I then moved forward and installed Wireshark, which allowed me to grab TCP data sent over our local network. This was to capture the data that was being sent from LGSVL to RViz in an attempt to use the data to see if our attack worked. When attempting to run multiple cars within LGSVL, our CPU cores would max utilization, and our RAM would follow, causing the program to crash and freeze the entire interface. I contacted ORC to have them increase our cores and ram for a 4th time, which allowed us to run a max of 3 cars without having any issues. We did have to deal with a lot of frame loss, causing laggy driving experiences. I then recorded, edited, and presented the demo with David. I then uploaded the demo to YouTube as it was a 2GB file that I could not easily share around.
