# Sentimental-Analysis
Web application made with flask to analyse sentiments of a twitter user based on his tweets (using Twitter API).

This application gets some of the tweets of the provided user name and perform a sentimental analysis using nltk based on good
and bad words. The result is then plotted using plotly :)

Usage:

```
 $ export API_KEY= <insert your API_KEY from Twitter here>
 $ export API_SECRET= <insert your API_SECRET from Twitter here>
 $ export FLASK_APP=application.py
 $ export FLASK_DEBUG=1
 $ flask run
```

![download](https://user-images.githubusercontent.com/19310512/37299623-d775c804-2649-11e8-964d-5b61a71cc6b2.png)

