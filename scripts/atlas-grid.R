library(ggplot2)
library(ggrepel)
library(lsr)

df = read.csv("city-list-count-10km-img-tz.csv")
df$tzcat = df$offset / 3600
df$latbin = cut(df$lat,9,labels=FALSE)
length(unique(df$tzcat)) # 18

df[c('tzcat','latbin')]

dfs = sortFrame(df,total_img)
dfs = dfs[1:64,]

ggplot(dfs,aes(tzcat,as.factor(latbin),label=Center)) + 
  geom_point(size=20,shape=1,color="darkgrey") +
  #geom_text_repel(size=8,color="grey") +
  scale_x_continuous(breaks=-8:10,
                     labels=-8:10) +
  theme(
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    panel.grid.major = element_line(color="white"),
    panel.grid.minor = element_line(color="white"),
    plot.background = element_rect(fill="white"),
    panel.background = element_rect(fill="white")
    ) +
  labs(x='',y='')

