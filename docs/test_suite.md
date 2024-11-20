# Test suite

Documents manual testing against the new platform to ensure all business as usual activities can be performed.

## Helpcentre CMS Platform

### 1. Adding articles to HelpCentre
- Access the admin area of the CMS (Content Management Service) at `/admin`.
- Click the icon 'Page', this sould take you to the page 'Home'.
- CLick the plus icon at the top of the page (next to the title 'Home'). It should have the tooltip 'Add child page'.
- Click 'Article index page', fill out the fields and then click 'Publish' below (default is 'Save draft').
![alt text](img/test_index.png "Test Index Article")

_Go to the home page and..._

**Check all fields entered in CMS are rendered** [x]
- In the `/admin` area, click on the article index page you have just created in 'Pages' (sidebar control).
- Click the elipsis icon (tooltip 'Actions') and select 'Add child page', then click 'Add article page'.
- Fill in the fields and click 'Publish'.
![alt text](img/test_article_summary.png "Test Index Article Summary")

_Click the Article Index Page..._

**Check all fields entered in CMS are rendered** [x]

![alt text](img/test_article_content.png "Test Index Article Content")

_Click the Article Page..._

**Check all fields entered in CMS are rendered** [x]

**Check this 'Was this page helpful?' widget renders** [x]

### 2. Modifying articles on HelpCentre
- Access the admin area.
- Find the article page you have created in `#1`.
- Amend the 'body' field and increment the 'sequence' field.

_Click the Article Page..._

![alt text](img/test_article_amended.png "Test Index Article Content Amended")

**Check all fields entered in CMS are rendered** [x]

**Check this 'Was this page helpful?' widget renders** [x]

### 3. Deleting articles on HelpCentre
- Access the admin area.
- Find the article page you have created in `#1`.
- Select delete when clicking 'action'.
- Confirm the delete.

**Check the page no longer appears in the index** [x]