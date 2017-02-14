df = read.csv("china_points.csv")

library(ggplot2)

ggplot(df,aes(lon,lat)) +
  borders(database = "world",
          regions = "china",
          colour="white",
          fill="grey75") +
  theme(panel.background = element_rect(fill="grey75"),
        panel.grid.major = element_line(color="grey75"),
        panel.grid.minor = element_line(color="grey75"),
        plot.background = element_rect(fill="grey75"),
        legend.position="none",
        axis.text = element_text(size=rel(0.1),color="white"),
        text = element_text(face="plain",color="white",size=15)) +
  geom_point(color="yellow",size=4,shape=1) + 
  labs(title='PRC')
