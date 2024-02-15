# Bookmarklets

## Browser URLs/address paths: HTTP, file:, javascript:

The address path in your browser can accept many more inputs than just links. One of these is javascript.

Try typing this directly into your URL bar:

```javascript
javascript:(function(){alert('Hello World')})()
```

*Note that you need to first wrap the function in () in order to run it. Otherwise you're just defining the function without telling it to run. You also need to already be at some sort of url already, typing this in an empty tab won't work.

## Writing a Bookmarklet
 
Now, bookmarks are basically just saved address paths, so you can also save javascript as bookmarks instead of conventional URLs. You can write your bookmarklet directly as the URL for a bookmark, but that can get confusing because it's all on one line. A more manageable way is to write them in an html doc, which is what we'll be doing.

Open the `starter.html` and start writing.

### Alert
First, let's just take what we previously wrote in our URL: 
```javascript
javascript:(function(){alert('Hello World')})()
```
in order for an html document to interpret our code as a link, we need place it into an `<a>` tag, like so:
```javascript
<a href="javascript:(function(){alert('Hello World')})()">Alert</a>
```

Note: From now on, be careful about your quotation marks! Everything will be placed inside the double quotations of `<a href="">`, so quotations inside need to be single quotations or else the browser will think you're ending your `href` prematurely.

### Change Background Color
Next, lets change the background color of the webpage.

Normally, you'd write your javascript like this:
```javascript
(function(){
    document.body.style.backgroundColor='red';
})()
```

but again, for the bookmarklet, you need to put the function into the `<a>` tag, like so: 
```javascript
 <a href="javascript:(function(){document.body.style.backgroundColor='red';})()">Change background color</a>
```

### Change Texts
We're going to try to change all the text on a given webpage. To do this, we can use a Javascript method called forEach().
forEach() allows you to run the same function on all the items in an array. There are 2 ways to write it:

```javascript
let array = document.querySelectorAll('div');
array.forEach(function(item) { /* ... */ })
```
OR
```javascript
array.forEach((item) => { /* ... */ })
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
Now put that into your `<a>` tag:

```javascript
<a href="javascript:
    (function() {
        let paragraphs = document.querySelectorAll('p');
        paragraphs.forEach((paragraph) => {
            paragraph.innerHTML='this is a bookmarklet now';
        });
    })()">Change texts</a>
```

### Change Images
Now we do the same for images.

```javascript
(function(){
    let images = document.querySelectorAll('img');
    images.forEach((img) => {
        img.src = 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Medium-Eva-Carriere-1912.jpg';
    })
})()
```

Again, put that into your `<a>` tag:

```javascript
<a href="javascript:
    (function(){
        let images = document.querySelectorAll('img');
        images.forEach((img) => {
            img.src = 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Medium-Eva-Carriere-1912.jpg';
        })
    })()">Change images</a>
```

Note: For your image, you need to choose an image with a stable URL hosted somewhere online. You can't just use an image on your computer, because the browser doesn't know how to find it.

