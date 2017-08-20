library(ggmap)
df = read.csv("London_geo.csv")

left = min(df$lon)
right = max(df$lon)
top = max(df$lat)
bottom = min(df$lat)

location = c(left,bottom,right,top)

basemap = ggmap(get_map(location=location,
                       source = "google",
                       maptype = "terrain",
                       color="bw"))

basemap + geom_point(data=df,
                    aes(lon,lat),
                    color="#1b79ff",
                    size=0.1,
                    shape=1) +
  theme(text=element_blank(),
        axis.text=element_blank(),
        axis.ticks=element_blank())

ggsave("zoom-london.png",
       width=72,
       height=72,
       units="in",
       limitsize=0)


