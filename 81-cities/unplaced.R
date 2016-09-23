df = read.csv("test_cw.csv")
library(ggplot2)

df$var = df$country_computed=='unplaced'


ggplot(df,aes(lon,lat,color=var)) +
  borders(database = "world",
          #regions = "china",
          colour="white",
          fill="grey75") +
  theme(panel.background = element_rect(fill="grey75"),
        panel.grid.major = element_line(color="grey75"),
        panel.grid.minor = element_line(color="grey75"),
        plot.background = element_rect(fill="grey75"),
        #legend.position="none",
        axis.text = element_text(size=rel(0.1),color="white"),
        text = element_text(face="plain",color="black",size=15)) +
  geom_point(size=1) + 
  labs(title='placed v unplaced')
