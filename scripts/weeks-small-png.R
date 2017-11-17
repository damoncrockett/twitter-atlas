pathstring = "/data/damoncrockett/twitter-atlas/spacetime/" 
targetpath = paste0(pathstring,"plots/")
setwd(pathstring)

df = read.csv("spacetime_week.csv")
library(ggplot2)

for (i in c(149:0)) {
    df = df[df$week <= i,]
    ggplot(df,aes(lon,lat)) +
        borders(database = "world",
                colour="grey45",
                fill="grey25",
                size=0.1) +
        theme(panel.background = element_rect(fill="grey65"),
              panel.grid.major = element_line(color="grey65"),
              panel.grid.minor = element_line(color="grey65"),
              plot.background = element_rect(fill="grey65"),
              legend.position="none",
              axis.text = element_blank(),
              text = element_blank(),
              axis.ticks = element_blank()) +
        geom_point(color = "#1b79ff",
                   size = 0.1)
    ggsave(paste0(targetpath,i,".png"),
           width = 6.4,
           height = 3.6,
           units = "in")
    print(i)
}