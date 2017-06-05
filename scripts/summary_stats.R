setwd("~/Desktop/twatl/")
library(ggplot2)

df = read.csv("summary_stats.csv")
n = nrow(df)
df$sizerankinv = rep(c(1:(n/2)),each=2)

ggplot(df,aes(sizerankinv,val50)) + geom_point() +
  stat_smooth()




vals = c("val10","val30","val50","val70","val90")
sats = c("sat10","sat30","sat50","sat70","sat90")
hues = c("hue10","hue30","hue50","hue70","hue90")

collist = append(c("city","year"),hues)

df = df[collist]

library(reshape2)
tmp = melt(df,id.vars=c("city","year"))

ggplot(tmp,aes(as.factor(year),
               value,
               group=variable)) +
  geom_line() +
  facet_wrap(~city)
