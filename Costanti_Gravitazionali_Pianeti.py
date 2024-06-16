print("---------------------------------------------------------------------");
print("Si consideri i seguenti pianeti con le loro caratteristiche . . .");
print("---------------------------------------------------------------------");

import second
import math
print("Di quale pianeta si vuole calcolare l'accellerazione di gravità : ");
print("Di quale pianeta si vuole calcolare la velocità di un satellite : ");
print("Di quale pianeta si vuole calcolare il periodo di rivoluzione di un satellite : ");
pianeta = input();
h1= input("Inserisci la distanza dalla superficie (m) : ");
h = float(h1);

if((pianeta=='mercurio')or(pianeta=='Mercurio')or(pianeta=='mercurio'.upper())):
   gravita = ((second.G*second.mercurio[0])/math.pow(second.mercurio[1],2));
   satellite = math.sqrt(second.G*second.mercurio[0]/second.mercurio[1]+h);
   periodo = (2*math.pi*(second.mercurio[1]+h))/satellite;
if((pianeta=='venere')or(pianeta=='Venere')or(pianeta=='venere'.upper())):
   gravita = ((second.G*second.venere[0])/math.pow(second.venere[1],2));
   satellite = math.sqrt(second.G * second.venere[0] / second.venere[1] + h);
   periodo = (2*math.pi*(second.venere[1]+h))/satellite;
if((pianeta=='terra')or(pianeta=='Terra')or(pianeta=='terra'.upper())):
   gravita = ((second.G*second.terra[0])/math.pow(second.terra[1],2));
   satellite = math.sqrt(second.G * second.terra[0] / second.terra[1] + h);
   periodo = (2*math.pi*(second.terra[1]+h))/satellite;
if((pianeta=='marte')or(pianeta=='Marte')or(pianeta=='marte'.upper())):
   gravita = ((second.G*second.marte[0])/math.pow(second.marte[1],2));
   satellite = math.sqrt(second.G * second.marte[0] / second.marte[1] + h);
   periodo = (2*math.pi*(second.marte[1]+h))/satellite;
if((pianeta=='giove')or(pianeta=='Giove')or(pianeta=='giove'.upper())):
   gravita = ((second.G*second.giove[0])/math.pow(second.giove[1],2));
   satellite = math.sqrt(second.G * second.giove[0] / second.giove[1] + h);
   periodo = (2*math.pi*(second.giove[1]+h))/satellite;
if((pianeta=='saturno')or(pianeta=='Saturno')or(pianeta=='saturno'.upper())):
   gravita = ((second.G*second.saturno[0])/math.pow(second.saturno[1],2));
   satellite = math.sqrt(second.G * second.saturno[0] / second.saturno[1] + h);
   periodo = (2*math.pi*(second.saturno[1]+h))/satellite;
if((pianeta=='urano')or(pianeta=='Urano')or(pianeta=='urano'.upper())):
   gravita = ((second.G*second.urano[0])/math.pow(second.urano[1],2));
   satellite = math.sqrt(second.G * second.urano[0] / second.urano[1] + h);
   periodo = (2*math.pi*(second.urano[1]+h))/satellite;
if((pianeta=='nettuno')or(pianeta=='Nettuno')or(pianeta=='nettuno'.upper())):
   gravita = ((second.G*second.nettuno[0])/math.pow(second.nettuno[1],2));
   satellite = math.sqrt(second.G * second.nettuno[0] / second.nettuno[1] + h);
   periodo = (2*math.pi*(second.nettuno[1]+h))/satellite;
print("accellerazione di gravità : ",gravita," m/^2");
print("velocità del satellite : ",satellite,"m/s",satellite*3.6," km/h");
minuti = periodo/second.COST;
min = float(minuti);
giorni = min/1440.0;
gio = float(giorni);
print("periodo di un satellite : ",periodo, "s","   equivalenti a : ",min," minuti ! ","  \n equivalenti a : ",gio," giorni ! ");







