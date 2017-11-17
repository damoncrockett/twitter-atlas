library(ggplot2)
library(tools)

basepath = "/data/damoncrockett/twitter-atlas/spacetime/"
sourcepath = paste0(basepath,"weeksquash/")
targetpath = paste0(basepath,"plots-medium/")
setwd(sourcepath)

l = list.files(sourcepath)

# First, the weeks that had squashing Antarctic outliers
for (filename in l) {
    df = read.csv(paste0(sourcepath,filename))
    basename = file_path_sans_ext(filename)
    ggplot(df,aes(lon,lat)) +
        borders(database = "world",
                colour="grey45",
                fill="grey25") +
        theme(panel.background = element_rect(fill="grey65"),
              panel.grid.major = element_line(color="grey65"),
              panel.grid.minor = element_line(color="grey65"),
              panel.border = element_blank(),
              plot.background = element_rect(fill="grey65",color="grey65"),
              legend.position="none",
              axis.text = element_blank(),
              text = element_blank(),
              axis.ticks = element_blank()) +
        geom_point(color = "#3388ff",
                   size = 0.01)
    ggsave(paste0(targetpath,basename,".pdf"),
           width = 64,
           height = 36,
           units = "in",
           limitsize = 0)
    print(basename)
}

# Now, the well-behaved weeks
sourcepath = paste0(basepath,"weeksunsquash/")
setwd(sourcepath)

l = list.files(sourcepath)

for (filename in l) {
    df = read.csv(paste0(sourcepath,filename))
    basename = file_path_sans_ext(filename)
    ggplot(df,aes(lon,lat)) +
        borders(database = "world",
                colour="grey45",
                fill="grey25") +
        theme(panel.background = element_rect(fill="grey65"),
              panel.grid.major = element_line(color="grey65"),
              panel.grid.minor = element_line(color="grey65"),
              panel.border = element_blank(),
              plot.background = element_rect(fill="grey65",color="grey65"),
              legend.position="none",
              axis.text = element_blank(),
              text = element_blank(),
              axis.ticks = element_blank()) +
        geom_point(color = "#3388ff",
                   size = 0.01)
    ggsave(paste0(targetpath,basename,".pdf"),
           width = 64,
           height = 36,
           units = "in",
           limitsize = 0)
    print(basename)
}