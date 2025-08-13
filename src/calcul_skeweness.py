import numpy as np
from stats_util import rec_moy,rec_variance,rec_ecart_type
def skeweness(height_list):
  n=len(height_list)
  et3=rec_ecart_type(height_list)**3
  moyenne=rec_moy(height_list)
  S=0
  for i in range (n):
    S+=(height_list[i]-moyenne)**3
    S= (n/(n-1)/(n-2))*S/et3
  return S
