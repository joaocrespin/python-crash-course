import requests
import plotly.express as px
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except:
        pass
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

clickable_titles, comments = [], []
for submission_dict in submission_dicts:
    titles = f'<a href="{submission_dict['hn_link']}">{submission_dict['title']}</a>'
    comments.append(submission_dict['comments'])
    clickable_titles.append(titles)

title = "Most Commented Posts on Hacker News"
labels = {'x': 'Title', 'y': 'Comments'}
fig = px.bar(x=clickable_titles, y=comments, title=title,
             labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.update_traces(marker_color='yellowgreen', marker_opacity=0.8)

fig.show()