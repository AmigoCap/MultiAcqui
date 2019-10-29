### TLDR

#### Maths de projection

Pour passer d'un repère 3D à un repère 2D on a besoin de 8 valeurs de projection :
(xx, xy, xz) : pour convertir un point en ordinnées
(yx, yy, yz) : pour convertir un point en abscices
(ox, oy) : les offsets entre les origines

Si (X, Y, Z) sont nos coordonnées 3D d'origine, alors on obtien les coordonnées projetées (X2d, Y2d) par :

X2d = X*xx + Y*xy + Z*xz + ox

Y2d = X*yx + Y*yy + Z*yz + oy


#### Pour ce qui nous concerne

Nos données sont : des coordonnées 3D obtenues en mocap et des coordonnées 2D obtenues par OpenPose.
On suppose dans un premier temps qu'on a des données synchronisées en temps.
Dans le cas où on n'a pas d'information sur la position de la caméra (i.e. : on n'a pas placé de marqueur dessus durant la mocap ni noté ses coordonnées), on peut l'approximer en utilisant la corrélation entre les données d'OpenPose et les données capteur.

On a N frames, et donc N positions 3D darticulation (mocap) et également N positions 2D (OpenPose). On peut donc inférer les 8 valeurs de projection par Machine Learning. On peut par exemple faire un algo génétique, voir un greedy algo.



#### Conclusion

Une descente de gradient gloutonne, associée à un gradient_step dynamique, donne des résultats corrects (mse : 36 pour un ordre de grandeur de 1000).

L'écart type moyen à la fin est autour de 25. Comme on ne semble pas pouvoir aller plus bas cela montre la différence entre la capture de la mocap et celle d'OpenPose.

Dans le premier cas d'essai, on obtient :

**Projection Matrix** : 
$$
\left(\begin{array} 
0.05241897 & -0.13417533 & -0.00497104\\
-0.00236236 &  0.00797051 & -0.25118345\\
\end{array}\right)
$$

**Offset Matrix** : 
$$
\left(\begin{array} 
1031.45356893\\
855.62283821\\
\end{array}\right)
$$