# Chrome Extensions

## Chrome extension boilerplate

The `starter` folder is a boilerplate chrome extension I downloaded off github. You'll notice it contains a number of javascript files, but for our purposes we'll only be working in the `after.js` and `manifest.json`.

## Naming the extension

First, name your extension by changing the default settings in the `manifest.json`:

```javascript
"name": "your project name here",
"description": "your description here",
```

Now let's try loading that into our Chrome extensions.

## Replacing images

Now, go to the after.js. This is the javascript that the extension runs after the page has loaded.
In here, let's try to replicate one of the functions in our bookmarklet:

```javascript
(function(){
    let images = document.querySelectorAll('img');
    images.forEach((img) => {
        img.src = 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Medium-Eva-Carriere-1912.jpg';
    })
})()
```

One nice thing about extensions is we won't have to wrap all our functions inside of `<a>` tags anymore.
Another is that we can use images that we have on our computer.
So, start by making a folder in your extension (called 'imgs' for example), and put an image of your choosing in it. (If you want, you can just use the "villainess.jpeg" I've put in the parent folder.)

```javascript
(function(){
    let images = document.querySelectorAll('img');
    images.forEach((img) => {
        img.src = 'imgs/villainess.jpeg';
    })
})()
```

But Chrome extensions access files with a special terminology, `chrome.runtime.getURL()`:

```javascript
img.src = chrome.runtime.getURL('imgs/villainess.jpeg');
```

Lastly, you also need to configure the image path in your `manifest.json`, or else the extension doesn't know where to look for the image. You need to add a section, `"web_accessible_resources"`, to your `manifest.json` and list your files inside it:
```javascript
"web_accessible_resources": [
    {"resources": ["imgs/villainess.jpeg"], "matches": ["<all_urls>"]}
]
```

## Pinpointing websites / Constraining the extension

Now, you might have noticed that the extension is running all the time, on every single webpage you visit, unless you disable the extension entirely. Maybe you only want to target one website in particular, or you don't want the extension to be affecting all your pages while you're still testing it. To limit the extension to run on just a select website(s), you need to edit the `"content_scripts"` in the `manifest.json`. 

You'll notice this snippet of code already there: 
```javascript
"matches": [
    "https://*/*",
    "http://*/*"
]
```
Basically, it's saying to run the corresponding javascript on any URL that matches anything. (* stands for anything)

To limit the extension to run only on, say the Smithsonian Collections, you change the `'matches'` to:
```javascript
"matches": [
    "https://*.si.edu/*",
    "http://*.si.edu/*"
]
```

With this, you can also start to create multiple different javascript files, doing different things, that run on different websites when they are "matched":

```javascript
{
    "run_at" : "document_idle",
    "js": ["after.js"],
    "matches": [
    "https://*.si.edu/*",
    "http://*.si.edu/*"
    ]
},
{
    "run_at" : "document_idle",
    "js": ["nypl.js"],
    "matches": [
    "https://*.digitalcollections.nypl.org/*",
    "http://*.digitalcollections.nypl.org/*"
    ]
}
```