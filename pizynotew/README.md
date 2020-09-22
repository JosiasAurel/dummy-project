
# Peasy Notes
This is a simple storage-less note taking app. All notes you write are stored in URLs (its the goal). 

When you write a note at the index and click ```save```, you will see a generated link below which is the URL to your note - But its not stored in any way!

## How it works
When you click the save button, your text is encoded in Base64 and given to you in the form ```http://domain.com/<base64-code>```.

When you open that link, my server converts the Base64 code back to its origin text and displays it on the page. Pretty Simple... isnt it ?

## Downsides
You can't make notes that include emojis - the app may freeze

### Further notes
I could have used other encoding algorithms like ```SHA-x``` or ```MD-x``` but i needed in a way it could be done on both front-end and back-end. That may remain a challenge for next time .

## Dependencies
- Bootstrap4
- Flask
- 


<a href="https://www.buymeacoffee.com/rocketstellar" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>