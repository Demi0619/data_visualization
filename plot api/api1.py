import requests
from plotly.graph_objs import Bar
from plotly import offline

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
response=requests.get(url,headers=headers)
status_code=response.status_code
#print(status_code)
response_dict=response.json()
print(response_dict.keys())
print('total items',response_dict['total_count'])
repo_dicts=response_dict['items']
print(f'returned reposiary:{len(repo_dicts)}')
repo_links,repo_star,repo_labels=[],[],[],
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    repo_star.append(repo_dict['stargazers_count'])
    repo_owner=repo_dict['owner']['login']
    repo_des=repo_dict['description']
    repo_label=f'{repo_owner}<br />{repo_des}'
    repo_labels.append(repo_label)

data=[
    {'type':'bar',
     'x':repo_links,
     'y':repo_star,
     'hovertext':repo_labels,
     'marker':
         {'color':'rgb(60,100,150)',
          'line':{'width':1.5,'color':'rgb(25,25,25)'}
          },
     'opacity':0.6,
     }
]
my_layout={
    'title':'most popular python repository',
    'titlefont':{'size':28},
    'xaxis':
        {'title':'repository name',
         'titlefont':{'size':24},
         'tickfont':{'size':10},
    },
    'yaxis':
        {'title':'stargazer number',
         'titlefont':{'size':24},
         'tickfont':{'size':10},},
}

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='most_popular.html')