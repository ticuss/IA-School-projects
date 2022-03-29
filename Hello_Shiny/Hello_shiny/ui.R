#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(colourpicker)
library(DT)
library(shinydashboard)
library(rAmCharts)
library(colourpicker)


# Define UI for application that draws a histogram
shinyUI(
  # navbarPage
  navbarPage("Hello World",
             
             # premier onglet Data
             tabPanel("Data", 
                      navlistPanel(
                        widths = c(2, 10), 
                        tabPanel("Table", 
                                 # titre avec css
                                 h1("Hello Shiny World", style = "color : #0099ff;text-align:center"),
                                 # table
                                 dataTableOutput("table")),
                        tabPanel("Summary",verbatimTextOutput("summary"))
                      )
             ), 
             
             # second onglet Visualisation
             tabPanel("Visualisation", 
                      
                      fluidRow(
                        # premier colonne
                        column(width = 3, 
                               # wellPanel pour griser
                               wellPanel(
                                 sliderInput("bins",
                                             "Number of bins:",
                                             min = 1,
                                             max = 50,
                                             value = 30),
                                 
                                 # input pour la couleur
                                 colourInput(inputId = "color", label = "Couleur :", value = "purple"),
                                 
                                 # titre du graphique
                                 textInput(inputId = "titre", label = "Titre :", value = "Histogramme"),
                                 
                                 # selection de la colonne
                                 radioButtons(inputId = "var", label = "Variable : ", choices = colnames(faithful)),
                                 
                                 downloadLink('download_plot', 'Télécharger le graphique'),

                                 # bouton
                                 actionButton("go", "GO!!!")
                               )
                        ), 
                        # deuxieme colonne
                        column(width = 9, 
                               tabsetPanel(id = "viz", 
                                 tabPanel("Histogramme", 
                                          # plotOutput -> amChartsOutput
                                          amChartsOutput("distPlot"),
                                          # classes (div centrée)
                                          div(textOutput("n_bins"), align = "center")
                                 ),
                                 tabPanel("Boxplot", amChartsOutput("boxplot"))
                               )
                        )
                      )
             ),
             
  )
)





# # Define UI for application that draws a histogram
# shinyUI(
# dashboardPage(
# dashboardHeader(title = "Hello dashboard"),
# dashboardSidebar("Hello from sideBar"),
# dashboardBody(
# # navbarPage
#     navbarPage("Hello APP STRUCTURE IN SHINY",

#         # premier onglet Data
#         tabPanel("Data", 
#                 navlistPanel(
#                 tabPanel("Table", dataTableOutput("table")),
#                 tabPanel("Summary",verbatimTextOutput("summary"))
#                 )
#         ), 
#         tabPanel("Visualisation", 
                
#                 fluidRow(
#                 column(width = 3, 
#                         wellPanel(
#                             sliderInput("bins",
#                                         "Number of bins:",
#                                         min = 1,
#                                         max = 50,
#                                         value = 30),
                            
#                             colourInput(inputId = "colors", label = "Couleur :", value = "purple"),
                            
#                             textInput(inputId = "titre", label = "Titre :", value = "Histogramme"),
                            
#                             radioButtons(inputId = "var", label = "Variable : ", choices = colnames(faithful))
#                         )
#                     ), 
#                         column(width = 9, 
#                                 tabsetPanel(
#                                     tabPanel("Histogramme", 
#                                             amChartsOutput("distPlot"),
#                                             div(textOutput("n_bins"), align = "center")
#                                     ),
#                                     tabPanel("Boxplot", plotOutput("boxplot"))
#                                             )
#                                 )
#                 )
#             ),
#             tabPanel("About",
#                     # rajout d'une image avec img()
#                     # elle doit etre dans www
#                     img(src = "./img/google-logo.png", width = 200),
#                     tags$hr(),
#                     "Press to go to google", 
#                     a(href = "www.google.fr", "GOOGLE"), 
#                     " HELLO GOOGLE.COM"
#             )   
#     )
# )
# )
# )



############### FIRST EXERCICE ##################
# # titlePanel("Old Faithful Geyser Data"),

#     # Sidebar with a slider input for number of bins
#     sidebarLayout(
#         sidebarPanel(
#             sliderInput("bins",
#                         "Number of bins:",
#                         min = 1,
#                         max = 50,
#                         value = 30),
#             selectInput(inputId = "colors", label = "Couleurs: ", 
#             choices = c("Rouge" = "red", "Vert" = "green", "Bleu" = "blue", "Jaune" = "yellow", "Grey" = "grey")),
#             textInput("titre", label = "Titre", value = "Hello shiny"),
#             radioButtons(inputId = "var", label = "Variable : ", choices = colnames(faithful)),
#             downloadLink('download_plot', 'Télécharger le graphique')

#         ),
    
#         # Show a plot of the generated distribution
#         mainPanel(
#             plotOutput("distPlot"),
#             div(textOutput("n_bins"), align = "center"),
#             dataTableOutput('table'),
#             datatable(faithful, style = 'bootstrap', editable = 'cell',   caption = 'This table is genereated using datatable function from DT library' )
#         )
#     ),
#     verbatimTextOutput("summary")



# tabPanel("About",
#                       # rajout d'une image avec img()
#                       # elle doit etre dans www
#                       img(src = "img/DATASTORM-GENES.jpg", width = 200),
#                       tags$hr(),
#                       "En tant que filiale du GENES, ", 
#                       a(href = "www.datastorm.fr", "DATASTORM"), 
#                       " valorise l’ensemble des 
#                       activités de recherche du Groupe auprès des entreprises et administrations."
#              )