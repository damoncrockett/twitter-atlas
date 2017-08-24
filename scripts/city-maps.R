library(ggmap)
setwd("~/Desktop/")
df = read.csv("London_geo.csv")


left = min(df$lon)
right = max(df$lon)
top = max(df$lat)
bottom = min(df$lat)

location = c(left,bottom,right,top)

locdf = data.frame(lon = c(left,right),
                   lat = c(bottom,top))

basemap = ggmap(get_map(location=location,
                       source = "stamen",
                       maptype = "toner-background"))

basemap + geom_point(data=locdf,
                    aes(lon,lat),
                    color="#1b79ff",
                    size=10,
                    alpha = 0.5) +
  theme(text=element_blank(),
        axis.text=element_blank(),
        axis.ticks=element_blank())



dfs = df[sample(nrow(df), 1000000), ]
qmplot(lon,lat,data=dfs,
       maptype="toner-background",
       darken=0.7,
       size = I(0.1),
       color = I("#1b79ff")) 
  
ggsave("zoom-london.png",
       width=72,
       height=72,
       units="in",
       limitsize=0)


