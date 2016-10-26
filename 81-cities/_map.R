library(ggplot2)

tmp = read.csv("81-cities-counts.csv")

ggplot(tmp,aes(lon,lat)) +
  borders(database = "world",
          #regions = "asia",
          colour="grey45",
          fill="grey25") +
  theme(panel.background = element_rect(fill="grey65"),
        panel.grid.major = element_line(color="grey65"),
        panel.grid.minor = element_line(color="grey65"),
        plot.background = element_rect(fill="grey65"),
        legend.position="none",
        axis.text = element_blank(),
        text = element_blank(),
        axis.ticks = element_blank()) +
  geom_point(aes(size=total_tweets_10km),alpha=0.5,color="dodgerblue") +
  scale_size_continuous(range=c(1,340))


max(tmp$total_tweets_10km) / min(tmp$total_tweets_10km)
