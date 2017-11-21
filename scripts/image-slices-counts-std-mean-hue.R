setwd("~/twitter-atlas/tables/")

#################
## sat and val ##
#################

df = read.csv("image-slices-counts-std-mean-hue.csv")
.3035409/131

head(df[order(df$nslices),],30)
head(df[order(df$meanval),])


tmp = df[df$year==2014,]
max(tmp$meanval)


#########
## hue ##
#########


d = read.csv("slice-agg-stats-hue.csv")
# first overall chi-squared gf

d$uniform = 0.125

d$c12 = as.integer( d$twelve * 10000 )
d$c14 = as.integer( d$fourteen * 10000 )

chisq.test(d$c12,p=d$uniform)
chisq.test(d$c14,p=d$uniform)
chisq.test(d$c12,d$c14)

