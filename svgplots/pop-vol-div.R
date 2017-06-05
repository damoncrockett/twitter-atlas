setwd("~/twitter-atlas")
d = read.csv("./tables/pop-vol-div-geo-sorted.csv")
df = read.csv("./tables/pop-vol-div-geo.csv")
df$diversity = df$actors / df$tweets
df$y = 1

d$label = paste0(d$city,"\n",d$country,sep="")
df$label = paste0(df$city,"\n",df$country,sep="")
df$label.order = factor(df$label,levels=as.vector(d$label))

library(ggplot2)

ggplot(df,aes(as.factor(year),y,alpha=diversity,size=tweets)) +
  geom_point(shape=16,color="dodgerblue") +
  facet_wrap(~label.order) +
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
  labs(x="",y="") +
  scale_size(range=c(1,71)) +
  geom_point(data=df,aes(as.factor(year),y,size=pop),shape=1,color="black",alpha=1)

