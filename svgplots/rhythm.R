setwd("~/Desktop/")
twelve = read.csv("secpast12.csv")
fourteen = read.csv("secpast14.csv")
df = read.csv("/Users/damoncrockett/twitter-atlas/tables/pop-vol-div-geo-sorted-label.csv")

library(ggplot2)

twelve$label = factor(twelve$label,levels=as.vector(df$label))
fourteen$label = factor(fourteen$label,levels=as.vector(df$label))

ggplot(twelve,aes(secpast)) + 
  geom_line(stat="density",linetype="dotted",color="grey25") +
  geom_line(data=fourteen,stat="density",color="grey25") +
  coord_polar() +
  facet_wrap(~label) +
  theme(
    text = element_text(family = "mono", 
                        face = "plain",
                        size = 28), 
    legend.position = "none",
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_blank(), 
    panel.border = element_blank(), 
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    axis.title.y = element_blank(),
    strip.background = element_blank(),
    strip.text = element_text(color="grey25")
  ) +
  labs(x="",y="")
