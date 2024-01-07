# MkDocs

## Why I decided to use MkDocs as a knowledge repository.

> 
> Ye shall know them by their fruits.
> Matthew 7:16

I came a across a web page [A gardening guide for your mind](https://www.mentalnodes.com/a-gardening-guide-for-your-mind)  which mentioned the following:

> A gardening guide for your mind
> 
> This is what a gardening guide for your mind would look like:
> 
> * **Seeds**. Seed your garden with quality content and cultivate your curiosity. Plant seeds in your mind garden by taking smart personal notes (taking raw notes is useless). These don't need to be written in a publishable form.
> * **Trees**. Grow your knowledge by forming new branches and connecting the dots. Write short structured notes articulating specific ideas and publish them in your digital garden. One note in your digital garden = one idea. (what you're currently reading is such a note) Do not keep orphan notes. Thread your thoughts.
> * **Fruits**. Produce new work. These are more substantial—essays, videos, maybe a book at some point. The kind of work researchers and creatives may hope will help them live beyond their expiration date.
> Networked thinking can happen at many levels. A digital garden is a scalable way to transform seeds of information into original work and to go from collector to creator.
> 

This made me realise that I have a huge and fairly well managed collection of seeds. I have notes and bookmarks for almost every site I have visited. I have collection of quotations from every book I have read on the Kindle over the last few years.

However I always felt that something was lacking.

I do also have, scattered around Internet, many Trees. Most are written in chats with friends or groups of acquaintances and are mind dumps on a topic that I was inspired to write at the time.

But, for all that work, I have no fruits of any consequence.

Some well known content creators have successfully gathered their articles_trees_ into a book _fruit_ or made a body of work, such as a collection of videos or pictures into a portfolio. Likewise the a collection of code into a project.

All of these have the common feature that they gathered their research into a collective whole and published it. 

I have had the feeling that this was the way to go for a long time but the article was what convinced me of it,

## So why MKDocs.

I did have blog of chronological links that I was publishing monthly but while the content was good it was a burden to do it monthly and also the method of retrieval wasn't useful for anyone. Nobody cares that I first found out about something last September, so a chronological blog doesn't fit the pattern that I want.

### I want something more like a wiki. 

The article above is published on a static site that based on TiddlyWiki. I like TiddlyWiki and it is extremely well done but after a couple of days I couldn't get the backend storage working on Github and on Node in a way that I wanted. I didn't want to the complexity of debugging a Node/JavaScript conversion to a static site.

All I want is a wiki that is based on Markdown written in a language that I am 100% comfortable with and for me that is Python. 

I have found other ways of doing this and I'm sure that I'll come back to those in future, if only to describe their good and bad points.

While I will probably write it is a blog, I want the flexibility to revise the articles and just keep the most relevant one on the web.

## Features

MKDocs has two features that I like. One I am yet to try.

### Web Server

The first is that it serves the files with a mini web servers so you can work locally and see your site as you write. You could use it this way just to have a local information repository.

### Save to Github Pages

The second is that it renders contents as static HTML which you can scp up to your site or you can set it up to deploy to Github pages. I redirected my static site to be hosted via Github using a custom domain and now I can run the command

```mkdocs gh-deploy```

to deploy the site. This automatically commits to the ```gh-pages``` branch and publishes to the site.

The Markdown files and any other files touched also need to be checked into Git on the ```main``` branch.

## Wiki Format

One thing that made it more attractive to me was that there is a Wiki plugin which worked right away. This automatically makes a link to the page with the same title as the WikiLink so is an easy way to make a Wiki like site. Clicking on a broken wiki link will lead to the standard 404 page so it is not a Wiki in the true sense of the word.

## Full Text Search

A feature that I wasn't expecting was full text search. I'm not sure exactly this works but I think that during the HTML creation the pages are tokenised an index created that allows a Javascript on the page to display they results. I'm not sure how this scales though.

## Extendibility

Looking at the api docs and the plugins documentation it seems that it is fully extensible in python {--*and though I probably won't*--}.

{{mymacro()}}

## Markdown Extensions

[PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/) has some nice extension to Markdown to add additional features to your editing. Such as *critic* to add {--*crossing out*--} and *emoji* to add emoji :rocket:. 

