#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(ggplot2)
library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
            
            h1("Iris", align = "center"),
            head(dataTableOutput("res_iris")),
            plotOutput('iris_plot'),
            h2("Histogramme", align = "center"),
            plotOutput('weight_plot'),
            plotOutput('glass_plot'),
            plotOutput('glass_reshaped_plot')
    )
)
