FunnyPages
==========

An app that allows you to curate a collection of webcomics that the app then checks for updates.  Skills applied include: Utilizing BeautifulSoup 4 to scrape raw html for img src parameters. Cloud based storage of static and media assets through an Amazon S3 bucket secured using IAM security tools and accessed through the Boto and Django-storages packages. Live ongoing deployment through Heroku, including a regularly scheduled (through Heroku Scheduler) custom manage.py command that periodically scrapes for the newest comic image url and downloads the associated file to S3 if it does not already exist there.  Front end work included all design including wireframing, final design in Adobe Photoshop, and image slicing.  All HTML and CSS was done from scratch with no templates.  It currently only supports a few comics. http://funnypages.herokuapp.com

NOTES:
 - The site is no longer live
 - I get asked a lot why I chose to download the image of the comic and reference it from my S3 storage instead of simply using the original url. The reason is that for some web comics the url for the image is dynamically generated and may not be the same from day to day, even though the name of the image file does.  This creates complications when trying to display the latest comic and determine if there was an update.  There were probably other ways to solve the issue, but as this was primarily an effort to learn about django for me I went this route so I could get more experience manipulating cloud based storage through my app.
