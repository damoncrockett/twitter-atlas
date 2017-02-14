df = read.csv("world_ua_bboxes_tweetcount.csv")
library(ggplot2)

df$total = df$tweet_count_2011 +
  df$tweet_count_2012 +
  df$tweet_count_2013 +
  df$tweet_count_2014

countries = c(
  "United States",
  "Mexico",
  "Colombia",
  "Argentina",
  "Peru",
  "Chile",
  "Brazil",
  "Canada",
  "Spain",
  "United Kingdom",
  "France",
  "Italy",
  "Turkey",
  "South Africa",
  "Egypt",
  "Russia",
  "Kuwait",
  "Saudi Arabia",
  "United Arab Emirates",
  "Thailand",
  "Malaysia",
  "Indonesia",
  "Singapore",
  "Philippines",
  "South Korea",
  "Japan",
  "Australia",
  "Ecuador",
  "Dominican Republic",
  "Venezuela",
  "Paraguay",
  "Portugal",
  "Ireland",
  "Nigeria",
  "Netherlands",
  "Belgium",
  "Germany",
  "Denmark",
  "Czech Republic",
  "Austria",
  "Sweden",
  "Hungary",
  "Serbia",
  "Poland",
  "Belarus",
  "Ukraine",
  "Greece",
  "Israel",
  "Jordan",
  "Lebanon",
  "Iraq",
  "Qatar",
  "Azerbaijan",
  "Pakistan",
  "India",
  "Kazakhstan",
  "Mongolia",
  "Vietnam",
  "China",
  "Taiwan"
)

cities = c(
  "Los Angeles",
  "Mexico City",
  "Bogota",
  "Buenos Aires",
  "Lima",
  "Santiago",
  "Rio de Janeiro",
  "Toronto",
  "Barcelona",
  "London",
  "Paris",
  "Rome", 
  "Istanbul", 
  "Cape Town", 
  "Cairo", 
  "Moscow",
  "Kuwait City",
  "Mecca", 
  "Dubai",
  "Bangkok", 
  "Kuala Lumpur",
  "Jakarta", 
  "Singapore", 
  "Manila", 
  "Seoul", 
  "Tokyo", 
  "Sydney", 
  "Guayaquil", 
  "Santo Domingo", 
  "Caracas", 
  "Asuncion", 
  "Lisbon", 
  "Dublin", 
  "Lagos", 
  "Amsterdam", 
  "Brussels", 
  "Berlin", 
  "Copenhagen", 
  "Prague",
  "Vienna",
  "Stockholm", 
  "Budapest", 
  "Belgrade", 
  "Warsaw", 
  "Minsk", 
  "Kiev",
  "Athens", 
  "Tel Aviv", 
  "Amman", 
  "Beirut", 
  "Baghdad", 
  "Doha", 
  "Baku", 
  "Karachi",
  "Mumbai", 
  "Almaty", 
  "Ulan Bator", 
  "Ho Chi Minh City", 
  "Beijing",
  "Taipei", 
  "San Juan", 
  "Guatemala City", 
  "San Salvador", 
  "San Jose", 
  "Panama City", 
  "Montevideo", 
  "Casablanca", 
  "Accra",
  "Abidjan", 
  "Dar es Salaam", 
  "Nairobi", 
  "Luanda", 
  "Sofia", 
  "Bucharest",
  "Helsinki",
  "Damascus", 
  "Manama",
  "Khartoum", 
  "Kampala", 
  "Phnom Pen", 
  "Dhaka" 
  )





tmp = df[c("Center","Country","lon","lat","Population","total")]
tmp = tmp[tmp$Center %in% cities,]
#tmp = tmp[!tmp$Country %in% countries,]

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
            axis.text = element_text(size=rel(0.1),color="grey45"),
            text = element_text(face="plain",color="grey45",size=15)) +
      #geom_point(aes(size=df$Population,color=df$tweet_count),alpha=0.5) +
      geom_text(label=tmp$Center,aes(size=tmp$Population,color=tmp$total)) + 
      labs(title='Global Urban Areas') + 
      scale_size(range=c(10,50)) + 
      scale_color_gradient2(midpoint=1000,
                            low="grey25",
                            mid="navyblue",
                            high="darkorange2",
                            space="Lab")

library(ggrepel)

ggplot(tmp,aes(lon,lat,label=Center)) +
  borders(database = "world",
          #regions = "asia",
          colour="grey45",
          fill="grey25") +
  theme(panel.background = element_rect(fill="grey65"),
        panel.grid.major = element_line(color="grey65"),
        panel.grid.minor = element_line(color="grey65"),
        plot.background = element_rect(fill="grey65"),
        legend.position="none",
        axis.text = element_blank()) +
  geom_text_repel(color="white",size=5,segment.color="white")

df_pct = read.csv("pct.csv")

ggplot(df_pct,aes(lon,lat,size=tweet_pct)) +
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
        axis.ticks.x = element_blank(),
        axis.ticks.y = element_blank()) +
  geom_point(alpha=0.25,color="dodgerblue") +
  scale_size(range=c(1,100))

size = c(1,2,4,8,16)
x = c(1,5,10,15,20)
y = c(1,1,1,1,1)

check = data.frame(size=size,x=x,y=y)

ggplot(check,aes(y,x,size=size)) + geom_point() + scale_size(range=c(1,16)) +
  theme(legend.position="none")

# okay so ggplot appears to map to area, not diameter; I'm guessing that if one data point 
# is twice another, it will have twice the area, although there has to be a fudge when 
# there aren't enough steps in the size scale








qplot(df$tweet_count[df$tweet_count<2500])

library(ggrepel)
ggplot(df,aes(total,Population,label=Center)) + 
  geom_text() + 
  stat_smooth()

ggplot(df,aes(tweet_count)) + geom_bar(binwidth=10000)
ggplot(df,aes(Population)) + geom_bar(binwidth=10000)

summary(lm(data=df,total~Population))

count_df = df[c(1,18:21)]
library(plyr)
d = rename(count_df, c("tweet_count"="2014",
                   "tweet_count_2013"="2013",
                   "tweet_count_2012"="2012",
                   "tweet_count_2011"="2011"))

d = d[c(1,5,4,3,2)]

library(reshape2)
count_df_melted = melt(d)
str(count_df_melted)

ggplot(count_df_melted,aes(variable,value,group=Center,color=Center)) + 
  geom_line() +
  theme(#panel.background = element_rect(fill="black"),
        #panel.grid.major = element_line(color="black"),
        #panel.grid.minor = element_line(color="black"),
        #plot.background = element_rect(fill="black"),
        legend.position="none",
        axis.text = element_blank(),
        text = element_blank())
        #axis.text = element_text(size=rel(0.1),color="white"),
        #text = element_text(face="plain",color="white",size=15))
