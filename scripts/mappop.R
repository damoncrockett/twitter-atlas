library(ggplot2)
df = read.csv("~/Desktop/100cities_subcontinents.csv")

df$totaltweets = rowSums(df[,c(5:39)])
  
ggplot(df,aes(lon,lat,size=totaltweets)) +
  borders(database = "world",
          colour="grey45",
          fill="grey25",
          size=.1) +
  theme(panel.background = element_rect(fill="grey65"),
        panel.grid.major = element_line(color="grey65"),
        panel.grid.minor = element_line(color="grey65"),
        plot.background = element_rect(fill="grey65"),
        legend.position="none",
        axis.text = element_blank(),
        text = element_blank(),
        axis.ticks = element_blank()) +
  geom_point(color = "#1b79ff",alpha=0.5) +
  scale_size_continuous(range=c(1,20))

ggsave("~/Desktop/check.png",width=6.4,height=3.6,units="in")
