\ Model NLP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  x2 + [ 2 x1 * y14 + 2 x2 * y14 + 2 x3 * y14 ] / 2 
Subject To
 Con1: [ y14 * y23 ] >= 20
 Con2: [ x1 ^2 + x2 ^2 + x3 ^2 + x4 ^2 ] = 30
 Con_y14: y14 + [ - x1 * x4 ] = 0
 Con_y23: y23 + [ - x2 * x3 ] = 0
Bounds
 1 <= x1 <= 3
 1 <= x2 <= 3
 1 <= x3 <= 3
 1 <= x4 <= 3
 y14 <= 300
 y23 <= 300
End
