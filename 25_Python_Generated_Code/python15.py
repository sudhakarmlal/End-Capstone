def cal_gforce ( mass1 : float , mass2 : float , distance : float ) -> float :
  g = 6.674 * ( 10 ) ** ( - 11 )
  return ( g * mass1 * mass2 ) / ( distance ** 2 )
