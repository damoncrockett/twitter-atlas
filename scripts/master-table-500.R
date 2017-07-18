setwd("~/twitter-atlas/tables")
df = read.csv("master-table-500-clean.csv")

library(reshape2)
library(ggplot2)

tweets = df[,c(1:39)]
actors = df[,c(1:4,40:74)]


mtweets = melt(tweets,id.vars=c("Center","Country","lat","lon"))
mactors = melt(actors,id.vars=c("Center","Country","lat","lon"))

ggplot(mtweets,aes(variable,value,group=Center)) + geom_line()
ggplot(mactors,aes(variable,value,group=Center)) + geom_line()
