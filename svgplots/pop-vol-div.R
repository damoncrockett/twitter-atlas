setwd("~/twitter-atlas")
df = read.csv("./tables/pop-vol-div.csv")
df$diversity = df$actors / df$tweets
df$y = 1

library(ggplot2)

ggplot(df,aes(as.factor(year),y,alpha=diversity,size=tweets)) +
  geom_point(shape=16,color="dodgerblue") +
  facet_wrap(~city) +
  theme(
    text = element_text(family = "mono", 
                        face = "plain"), 
    legend.position = "none",
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    panel.background = element_blank(), 
    panel.border = element_blank(), 
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    axis.title.y = element_blank(),
    strip.background = element_blank(),
    strip.text = element_text(color="grey25")
  ) +
  labs(x="",y="") +
  scale_size(range=c(1,179))


theme(
  line = element_line(colour = "black", size = 0.5, linetype = 1, lineend = "butt"), 
  rect = element_rect(fill = "white", colour = "black", size = 0.5, linetype = 1), 
  
  axis.text = element_text(size = rel(0.8), colour = "grey50"), 
  strip.text = element_text(size = rel(0.8)), 
  axis.line = element_blank(), 
  axis.text.x = element_text(vjust = 1), 
  axis.text.y = element_text(hjust = 1), 
  axis.ticks = element_line(colour = "grey50"), 
  axis.title.x = element_text(), 
  axis.title.y = element_text(angle = 90), 
  axis.ticks.length = unit(0.15, "cm"), 
  axis.ticks.margin = unit(0.1, "cm"), 
  
  legend.background = element_rect(colour = NA), 
  legend.margin = unit(0.2, "cm"), 
  legend.key = element_rect(fill = "grey95", colour = "white"), 
  legend.key.size = unit(1.2, "lines"), 
  legend.key.height = NULL, 
  legend.key.width = NULL, 
  legend.text = element_text(size = rel(0.8)), 
  legend.text.align = NULL, 
  legend.title = element_text(size = rel(0.8), face = "bold", hjust = 0), 
  legend.title.align = NULL, 
  legend.position = "right", 
  legend.direction = NULL, 
  legend.justification = "center", 
  legend.box = NULL, 
  
  
  panel.margin = unit(0.25, "lines"), 
  panel.margin.x = NULL, 
  panel.margin.y = NULL, 
  
  strip.background = element_rect(fill = "grey80", colour = NA), 
  strip.text.x = element_text(), 
  strip.text.y = element_text(angle = -90), 
  
  plot.background = element_rect(colour = "white"), 
  plot.title = element_text(size = rel(1.2)), 
  plot.margin = unit(c(1, 1, 0.5, 0.5), "lines"), complete = TRUE)