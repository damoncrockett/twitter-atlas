setwd("~/twitter-atlas/tables/")
df = read.csv("image-data-histograms_columnized-merged.csv")
d = read.csv("image-slices-counts-std-mean-hue.csv")

library(ggplot2)
library(reshape2)

d = d[d$year==2014,]
d = d[,c("city","nslices")]
tmp = d[d$nslices > 67000,]
temp = df[df$city %in% tmp$city,]
unique(temp$city)

df.melted = melt(temp,id.vars=c("city","year"))

hsvbins = unique(df.melted$variable)
vals = hsvbins[1:10]
sats = hsvbins[11:20]
hues = hsvbins[21:28]

levels(df.melted$variable)

ggplot(df.melted[df.melted$variable %in% vals,],
       aes(as.factor(year),value,group=variable,color=variable)) + 
  geom_line(size=5) +
  facet_wrap(~city) +
  scale_color_manual(values=c("grey0",
                              "grey11",
                              "grey22",
                              "grey33",
                              "grey44",
                              "grey55",
                              "grey66",
                              "grey77",
                              "grey88",
                              "grey99")) +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    plot.background = element_rect(fill="grey25"),
    panel.background = element_rect(fill="grey25"),
    legend.key = element_rect(fill=NA,color=NA),
    legend.title = element_blank(),
    legend.background = element_blank(),
    legend.box = NULL,
    strip.background = element_blank(),
    axis.title = element_blank(),
    strip.text = element_text(color="white",size=16),
    text = element_text(color="white",size=16),
    axis.text.x = element_text(color="white",size=16),
    axis.text.y = element_blank(),
    legend.position = "none",
    #axis.ticks = element_line(color="white")
    axis.ticks = element_blank()
    )

#ggsave("~/Desktop/Rplot.svg",width=4,height=4,units="in")

ggplot(df.melted[df.melted$variable %in% hues,],
       aes(as.factor(year),value,group=variable,color=variable)) + 
  geom_line(size=5,alpha=0.5) +
  facet_wrap(~city) +
  scale_color_manual(values=c("red",
                              "orange",
                              "yellow",
                              "green",
                              "cyan",
                              "blue",
                              "purple",
                              "magenta")) +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    plot.background = element_rect(fill="grey25"),
    panel.background = element_rect(fill="grey25"),
    legend.key = element_rect(fill=NA,color=NA),
    legend.title = element_blank(),
    legend.background = element_blank(),
    legend.box = NULL,
    strip.background = element_blank(),
    axis.title = element_blank(),
    strip.text = element_text(color="white",size=16),
    text = element_text(color="white",size=16),
    axis.text = element_text(color="white",size=16),
    axis.ticks = element_line(color="white")
  )

ggplot(df.melted[df.melted$variable %in% sats,],
       aes(as.factor(year),value,group=variable,color=variable)) + 
  geom_line(size=5,alpha=0.5) +
  facet_wrap(~city) +
  scale_color_manual(values=c("#8f8f8f",
                              "#828f9b",
                              "#7690a7",
                              "#6a90b4",
                              "#5d90c0",
                              "#5191cd",
                              "#4591d9",
                              "#3892e5",
                              "#2c92f2",
                              "#1f93ff")) +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    plot.background = element_rect(fill="grey25"),
    panel.background = element_rect(fill="grey25"),
    legend.key = element_rect(fill=NA,color=NA),
    legend.title = element_blank(),
    legend.background = element_blank(),
    legend.box = NULL,
    strip.background = element_blank(),
    axis.title = element_blank(),
    strip.text = element_text(color="white",size=16),
    text = element_text(color="white",size=16),
    axis.text = element_text(color="white",size=16),
    axis.ticks = element_line(color="white")
  )
