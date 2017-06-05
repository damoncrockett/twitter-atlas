setwd("~/Desktop/")
m = read.csv("Manama_2014_sampled.csv")
k = read.csv("Kiev_2014.csv")

ms = subset(m,m$huepeak!=0)
ks = subset(k,k$huepeak!=0)
  
library(ggplot2)

ggplot(ms,aes(huepeak)) + 
  geom_histogram(binwidth=25,
                 fill="grey",
                 #color="black",
                 alpha=0.5) +
  theme(
    legend.position = "none",
    text = element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_rect(fill="white"),
    panel.grid.minor = element_line(color="white"),
    panel.grid.major = element_line(color="white"),
    plot.background = element_rect(fill="white",color=NA)
    ) +
  geom_histogram(data=ks,
                 binwidth=25,
                 color="black",
                 alpha=0) +
  coord_polar()