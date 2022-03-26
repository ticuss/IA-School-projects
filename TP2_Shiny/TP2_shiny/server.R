#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(easyGgplot2)
library(shiny)
library(dplyr, quietly = TRUE)
library(plyr)
library(mlbench)
library(reshape2)
data(Glass)


# Define server logic required to draw a histogram
shinyServer(function(input, output) {
    
    output$weight <- renderDataTable(weight)
    
    output$res_iris <- renderDataTable(iris)
    
    output$iris_plot <- renderPlot(
        ggplot(iris)+aes
        (
            x = Sepal.Width,
            y = Sepal.Length,
            color = Species,
            shape = Species 
        )
            + geom_point() 
            + facet_grid(~Species) 
            + theme_dark() 
            + stat_smooth(method = "lm")
    )
    
    cmean <- weight %>% group_by(sex)%>% summarise(mean = mean(weight))
    
    mu <- ddply(weight, "sex", summarise, grp.mean=mean(weight))
    
    output$weight_plot <- renderPlot(
        ggplot(weight, aes(x=weight, color=sex)) +
        geom_density(fill="white") + 
        geom_vline(data=mu,
            aes(
                xintercept=grp.mean, color=sex
                ),
            linetype="dashed")+
            scale_color_manual(values=c("#999999", "#E69F00", "#56B4E9"))+
            scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9")) + 
            theme(legend.position="right")
    )
    output$glass <- renderDataTable(Glass)
    

    output$glass_plot <-renderPlot(
        ggplot(Glass, aes(x = Type, y = Ca, fill = Type)) 
        + geom_boxplot() 
        + scale_color_brewer(palette="Dark2") 
        + scale_fill_brewer(palette="Dark2") 
        + labs(title="Glass plot ")
    )

    output$glass_reshaped_plot <- renderPlot(
        ggplot(
            reshape2::melt(Glass[,6:10], id.vars = "Type"),
            aes( 
                x = variable, y = value, fill = Type
                )
                ) 
        + geom_boxplot()
        + facet_wrap( ~ variable, ncol=2, scales = "free")
    )   
}
)
