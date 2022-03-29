
#########---TP1---#########

#--- EX1 Etude sur l'indice de la masse corporelle 

# Read data 
data <- read.csv("~/Documents/TP1_EX1.csv", sep = ";")
nutriage <- read.csv("~/Documents/TP1_EX1.csv", sep = ";")

# Transpose data

# Assign the first column as a varable  and the first line 
attach(data) 

Individus <- data$Prénom  
Individus
Poids
Taille
Sexe
length(Taille)
data <- data[-11,]
data
Taille
moyenne_taille <- mean(Taille[1 : 10])
moyenne_taille
moyenne_pois <- mean(Poids[1 : 10])

IMC <- function(taille, poids){
  imc <- round((poids / taille^2),5)
  return (imc) 
}

IMC_vector <-IMC(Taille,Poids)
IMC_vector
Taille
plot(Poids, Taille, main = "Nuage de points en fonction de la taille", xlab="Poids", ylab="Taille")

#----- EX2: Importer des données depuis un fichier texte ASCII

data2 <- read.table("OneDrive - ENGIE/Statistique/nutriage.txt",header=T,sep="\t",dec=".")
library(DT)
datatable(donnees, options = list(pageLength = 10))

attach(data2)

#Question : Combien y-a-t-il de variables ? Combien y-a-t-il d’invidus ?
# 226 variables et 13 Individus


#Question : Comment les personnes de cet échantillon utilisent les matières grasses pour cuisiner ?
  quotMatGras = data2["matgras"]
  sum(quotMatGras > 0) # = 226 utilisent les matières grasses pour cuisiner
  
#Question : Combien de personnes mangent quotiennement de la viande ?
#Select row of "Viande"
quotViande = data2["viande"]
#Sum of people that eats more than 7 times meat 
sum(quotViande >= 7) # = 0 


res<-hist(taille,plot=F)
nn<-as.character(res$breaks)
x<-as.table(res$counts) 
dimnames(x)<-list(paste(nn[-length(nn)],nn[-1],sep="-"))
x

#Question : Combien y-a-t-il d’individus dont la taille est dans l’intervalle ]155,160] ?
# il y a 50 des individus

matable<-table(sexe,situation)
matable
hommes = sum(head(matable,1))
femmes = sum(matable[2,])
femmes

# Question : Dans cet échantillon de 226 individus, quel est le pourcentage d’hommes vivant en couple ?

percentageOfMarriedMen = (20/226)*100
percentageOfMarriedMen

matable_complete <- addmargins(matable)
matable_complete

#Question : Parmi les hommes, quel est le pourcentage d’homme vivant en couple ?

percentageOfMarriedMenOfTotalMen = (20/hommes)*100
percentageOfMarriedMenOfTotalMen

# Question : Combien d’invidus mesurent strictement moins que la médiane et combien mesurent strictement plus que la médiane ?
tailleMoyenne = median(taille)
 toto<-subset(taille, taille < tailleMoyenne)
 titi<-subset(taille, taille > tailleMoyenne)
individusPlusPetitsQueLaMoyenne = nrow(toto)
individusPlusPetitsQueLaMoyenne
individusPlusGrandsQueLaMoyenne = nrow(titi)
individusPlusGrandsQueLaMoyenne

# Exercices *
#1) Faire une fonction qui simule le lancement d’une pièce (résultat pile ou face).
coin <- c("face", "pile")
coin
sample(coin, size = 1)

# Faire une fonction qui simule le lancement d’un dé à 6 faces (avec la fonction sample()).
die <- c(1,2,3,4,5,6)
rolldice <- function() {
  simulation = (sample(die, size = 6, replace = TRUE))
  return (simulation)
}
#Simuler le jeu de Yams (lancer de 5 dés simultanément) en utilisant les paramètres size et replace de la fonction sample().
rollFiveDices <- function() {
  fiveDice = replicate( 5 ,rolldice())
  return (fiveDice)
}

#Estimer la probabilité d’obtenir un yams en utilisant les fonctions apply(), replicate() et unique(). Comparer à la valeur théorique.


# Function that loops through the array returns a true only if all the values are the same 
isYams <- function(x) length(unique(x)) == 1


size = 100000

# Creating simulations by throwing the dies depending of the variable size 
simulations = replicate(size,rollFiveDices())
simulations
# function that loops through all our simulation and looks how many yams we achieve that returns the sum of yams of our simulation 
simulate <- function(){
  totalYams <- c()
for (i in 1:size){
  yam <- c()
  for(j in 1:ncol(simulations)){
    yam <-c(yam,isYams(simulations[ , j , i]))
  }
  if(sum(yam) > 0) { 
    totalYams <- c(totalYams, 1)
    print(totalYams)
    }
}
  return (sum(totalYams))
}

rollFiveDices()
probability = (simulate()/size)
probability
# Not sure if it's correct, hope that we will se the sulution at the course.  
probabilityOneRoll = 1/6 * 1/6* 1/6 * 1/6 * 1/6* 1/6
probabilityFiveRoll = 5* probabilityOneRoll
probabilityFiveRoll
theoreticProbability = size * probabilityFiveRoll
theoreticProbability 
a = 10 
print(a)



