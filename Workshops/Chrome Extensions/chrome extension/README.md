# Chrome Extensions

## Chrome extension boilerplate

The fresh-chrome-extension-main folder is a boilerplate chrome extension I downloaded off github. You'll notice it contains a number of javascript files, but for our purposes we'll only be working in the `after.js`, which runs after the page has loaded.

Try typing this directly into your URL bar:

```javascript
javascript:(function(){alert('Hello World')})()
```

*Note that you need to first wrap the function in () in order to run it. Otherwise you're just defining the function without telling it to run. You also need to already be at some sort of url already, typing this in an empty tab won't work.

## Writing a Bookmarklet
 
You can write your bookmarklets directly as URLs for bookmarks, but that can get confusing because it's all on one line. You can also write them in an html, which is what we'll be doing.
Note: Be careful about your quotation marks! Everything will be placed inside the double quotations of <a href="">, so quotations inside need to be single quotations or else the browser will think you're ending your `href` prematurely.

Open the starter.html and start writing.

### Alert
First, let's just take what we previously wrote in our URL: 
```javascript
javascript:(function(){alert('Hello World')})()
```
and place it into an <a> tag, like so:
```javascript
<a href="javascript:(function(){alert('Hello World')})()">Alert</a>
```

### Change Background Color
Next, lets change the background color of the webpage.

Normally, you'd write your javascript like this:
```javascript
(function(){
    document.body.style.backgroundColor='red';
})()
```

but for the bookmarklet, you need to put the function into the <a> tag, like so: 
```javascript
 <a href="javascript:(function(){document.body.style.backgroundColor='red';})()">Change background color</a>
```

### Change Texts
We're going to try to change all the text on a given webpage.
Firstly: forEach() is a JS method that allows you to run the same function on multiple items in an array. There are 2 ways to write it:

```javascript
let array = document.querySelectorAll('div');
array.forEach(function(currentElement) { /* ... */ })
```
OR
```javascript
array.forEach((currentElement) => { /* ... */ })
```

So, to change all the texts on a webpage, we'd write this:
```javascript
(function() {
    let paragraphs = document.querySelectorAll('p');
    paragraphs.forEach((paragraph) => {
        paragraph.innerHTML='this is a bookmarklet now';
        });
})()
```
Now put that into your <a> tag.


### Change Images
Now we do the same for images.

```javascript
(function(){
    let images = document.querySelectorAll('img');
    const newImg = new Image;
    newImg.src = 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Medium-Eva-Carriere-1912.jpg';
    images.forEach((img) => {
        img.src = newImg.src;
        })
})()
```
Note: For your image, you need to choose an image with a stable URL hosted somewhere online. You can't just use an image on your computer.


```javascript

```
