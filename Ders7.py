while (True):
  ser1=input(" notunuzu giriniz please:")
  if ser1 == "q" or "Q":
    ser1=int(ser1)
  elif ser1>=85:
   print("taktir")
  elif ser1>=84 and ser1<=70:
    print("teşekkür")
  else:
   print("hayırsız evlat") 