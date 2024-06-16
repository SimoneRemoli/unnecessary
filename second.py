import math
m1 = 3.285*(math.pow(10,23)); #mercurio
r1 = 2440000; #KM
###
m2 = 4.867*(math.pow(10,24));
r2 = 6052000; #KM
###
m3 = 5.972*(math.pow(10,24));
r3 = 6371000; #KM
###
m4 = 6.4*(math.pow(10,23));
r4 = 3390000; #KM
###
m5 = 1.898*(math.pow(10,27));
r5 = 69911000; #KM
###
m6 = 5.683*(math.pow(10,26));
r6 = 58232000; #KM
###
m7 = 8.681*(math.pow(10,25));
r7 = 25362000; #KM
###
m8 = 1.024*(math.pow(10,26));
r8 = 24622000; #KM

G = 6.67*(math.pow(10,-11));
COST = 60.0;
print(" Costante gravitazionale : ",G);
#--Creazione delle liste contenenti i dettagli dei singoli pianeti--
mercurio = [m1,r1];
venere = [m2,r2];
terra = [m3,r3];
marte = [m4,r4];
giove = [m5,r5];
saturno = [m6,r6];
urano = [m7,r7];
nettuno = [m8,r8];
#---------------------------------------------------------------------
#formula per il calcolo dell'accellerazione di gravità : g = G(Cost)*M(massa pianeta)/R^2(raggio)
#----------------------------
print(" Nome        massa(kg)       raggio(m)");
print("Mercurio = ",mercurio[0],mercurio[1]);
print("Venere = ",venere[0],venere[1]);
print("Terra = ",terra[0],terra[1]);
print("Marte = ",marte[0],marte[1]);
print("Giove = ",giove[0],giove[1]);
print("Saturno = ",saturno[0],saturno[1]);
print("Urano = ",urano[0],urano[1]);
print("Nettuno = ",nettuno[0],nettuno[1]);

