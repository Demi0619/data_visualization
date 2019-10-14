import requests
from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f'get ID status:{r.status_code}')
id_dict=r.json()
home_dicts=[]
for id in id_dict[:30]:
    url2=f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    r2=requests.get(url2)
    #print(f'get {id}status{r2.status_code}')
    info_dict=r2.json()
    home_dict={
        'title':info_dict['title'],
        'comments':info_dict['descendants'],
        'newslink':f"http://news.ycombinator.com/item?id={id}"
    }
    home_dicts.append(home_dict)
    home_dicts=sorted(home_dicts,key=itemgetter('comments'),reverse=True)
news_links,news_comments=[],[]
for home_dict in home_dicts:
    news_comments.append(home_dict['comments'])
    news_title=home_dict['title']
    news_url=home_dict['newslink']
    news_link=f"<a href='{news_url}'>{news_title}</a>"
    news_links.append(news_link)

data={
    'x':news_links,
    'y':news_comments,
    'type':'bar'
}
my_layout={
    'title':'top 30 news',
    'titlefont':{'size':30,},
    'xaxis':{
        'title':'news name',
        'titlefont':{'size':20},
        'tickfont':{'size':10},
    },
    'yaxis':{
        'title':'comments of news',
        'titlefont':{'size':20},
        'tickfont':{'size':10}
    }
}
fig={
    'data':data,'layout':my_layout
}
offline.plot(fig,filename='top_news.html')