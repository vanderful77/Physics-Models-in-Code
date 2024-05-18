## Goal

Simulate an arbitrary initial circumstance and see what happens

## Constants

$l_1 = 4$

$l_2 = 2$

$m_1 = 4$

$m_2 = 8$

$g = 9.8$

Duration: $20$s

Framerate: $25$fps

## Initial Values

$\theta_1=\pi/3$

$\theta_2=2\pi/3$

$$\dot{\theta_1}=0$$ 

$\dot{\theta_2}=0$

## Results

![image-20240406031726939](C:\Users\33779\AppData\Roaming\Typora\typora-user-images\image-20240406031726939.png)

![image-20240406031732668](C:\Users\33779\AppData\Roaming\Typora\typora-user-images\image-20240406031732668.png)

In which $ME$ stands for mechanical energy, $T$ stands for kinetic energy, $V$ stands for potential energy



The theoretical mechanic energy is $-156.8000000000001$ J 

The average calculated mechanical energy is $-149.105709122475$ J

The Root Mean Square Error of mechanical energy is $8.99306593394937$

the standard deviation of mechanical energy is  $0.013152562107351965$

Therefore the calculated energy stays close to the theoretical energy, meaning the energy of this system converges to the theoretical value. Compared with trail 4, the theoretical energy are the same, yet the motion of this is less complex and the accuracy and preciseness are higher. We can infer the reason to be a truncation error. The further research with focus on the effect of increasing sampling interval on precision. This simulation has a high accuracy and a high preciseness. 