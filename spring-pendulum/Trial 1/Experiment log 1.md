## Goal

Simulate a rigid spring, test if the system regress to a simple pendulum

## Constants

$k = 1000000$

$l_0 = 1$

$m = 1$

$g = 9.8$

Duration: $20$s

Framerate: $25$fps

## Initial Values

$l=1$

$\dot{l}=0$

$$\theta=1$$ 

$\dot{\theta}=0$

## Results

![image-20240406010133912](C:\Users\33779\AppData\Roaming\Typora\typora-user-images\image-20240406010133912.png)

![image-20240406010142765](C:\Users\33779\AppData\Roaming\Typora\typora-user-images\image-20240406010142765.png)

In which $ME$ stands for mechanical energy, $T_{rad}$ stands for radical kinetic energy, $T_{tan}$ stands for tangential kinetic energy, $V_{elas}$ stands for elastic potential energy, $V_{grav}$ stands for gravitational potential energy. 



The theoretical mechanic energy is -5.29496259750777$ J 

The average calculated mechanical energy is $-5.294566261432506$ J

The Root Mean Square Error of mechanical energy is $0.0006054924267830725$

the standard deviation of mechanical energy is  $5.1269542692886235e-05$

Therefore the calculated energy stays close to the theoretical energy, meaning the energy of this system converges to the theoretical value.  This simulation has a high accuracy and a high preciseness. 