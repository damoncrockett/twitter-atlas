setwd("~/Desktop/")
twelve = read.csv("secpast12.csv")
fourteen = read.csv("secpast14.csv")
df = read.csv("/Users/damoncrockett/twitter-atlas/tables/pop-vol-div-geo-sorted-label.csv")

library(ggplot2)

df <- df[order(df$tweets),]

twelve$label = factor(twelve$label,levels=as.vector(df$label))
fourteen$label = factor(fourteen$label,levels=as.vector(df$label))

ggplot(twelve,aes(secpast)) + 
  geom_line(stat="density",
            color="grey25",
            adjust=1) +
  geom_line(data=fourteen,
            stat="density",
            color="grey25",
            linetype="dotted",
            adjust=1) +
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

c = df$label[33:81]

twelve.t = twelve[twelve$label %in% c,]
fourteen.t = fourteen[fourteen$label %in% c,]

ggplot(twelve.t,aes(secpast,..density..)) + 
  geom_histogram(bins=168,fill="blue",alpha=0.5) +
  geom_histogram(data=fourteen.t,bins=168,fill="orange",alpha=0.5) +
  #geom_density(bw=10000,color="blue") +
  #geom_density(data=fourteen.t,bw=10000,color="orange") +
  #coord_polar() +
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
