setwd("~/Desktop/twatl/")
df = read.csv("Guayaquil_2012.csv")
d = read.csv("Guayaquil_2014.csv")
library(ggplot2)

ggplot(df,aes(val)) + 
  geom_density(linetype="solid",
               color="grey75",
               size=1) +
  geom_density(data=d,
               aes(val),
               linetype="dotted",
               color="orange",
               size=1) +
  theme(
    text = element_text(family = "mono", 
                        face = "plain"), 
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

ggplot(df,aes(val)) + 
  geom_line(stat="density",
            linetype="solid",
               color="grey75",
               size=1) +
  geom_line(data=d,
               aes(val),
            stat="density",
               linetype="dotted",
               color="orange",
               size=2) +
  theme(
    text = element_text(family = "mono", 
                        face = "plain"), 
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


