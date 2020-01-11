# URL Shortener

URLs can be extremely long and not user-friendly, when sharing URLs, it's always nicer and easier to share them with short form factor, even memorize them!
This is where the URL Shortener comes in. A URL Shortener reduces the characters or letters in a URL, making them easier to read and remember. A URL like:
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CC4QFjAA&url=http%3A%2F%2Fthelongestlistofthelongeststuffatthelongestdomainnameatlonglast.com%2Fwearejustdoingthistobestupidnowsincethiscangoonforeverandeverandeverbutitstilllookskindaneatinthebrowsereventhoughitsabigwasteoftimeandenergyandhasnorealpointbutwehadtodoitanyways.html&ei=40egUo2MGI3xoATQtIKwDQ&usg=AFQjCNHbBa5Fk4YutdUOj_D8IwpJLu7hGw&sig2=8P4ew1Yie72Ps_OQ-L5cXw&bvm=bv.57155469,d.cGU
becomes:
https://www.google.com/IS


# **Examples of URL Shorteners**

Here are some implementations of the URL Shortener idea:

-   [Bitly](https://bitly.com/)
-   [MeShort](http://www.msht.us/)

## **Technical Details**

I used only packages coming with Python
	- random
	- urllib
	- json
	- string
Flat JSON file is used as "database" to verify duplicate URLs don't get generated, there is also character number selector with the function.

