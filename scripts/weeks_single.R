basepath = "/data/damoncrockett/twitter-atlas/spacetime/"
sourcepath = paste0(basepath,"weeks/")
targetpath = paste0(basepath,"plots/")
setwd(sourcepath)

library(ggplot2)

for (i in c(149:0)) {
    df = read.csv(paste0(i,".csv"))
    ggplot(df,aes(lon,lat)) +
        borders(database = "world",
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
        geom_point(color = "#1b79ff",
                   size = 0.1)
    ggsave(paste0(targetpath,i,".png"),
           width = 64,
           height = 36,
           units = "in",
           limitsize = 0)
    print(i)
}