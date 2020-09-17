# Uniqlo Alarm

aka how to get your Nezuko/Zenitsu/other highly desired UT collab shirts without knowing when they'll restock exactly (esp early in the morning)

the wonders of 6 am salty coding...

## Usage

Mac only (sorry PC users)...

1. Download this project (see the Git clone on the righthand corner or in Terminal run `git clone https://github.com/chenboy3/uniqlo_alarm.git`)
2. Make sure you have Python3 installed (run `python3 -- version` and see what version Python you have)
3. Leave your computer plugged in, make sure it won't go to sleep (turn off the display if you have to), max volume (or however loud you need it to wake you up in the middle of the night)
4. Open Terminal, navigate to this folder.
5. Run the virtual environment with `./bin/activate`
6. `python3 crawler.py`
7. Wait for the "alarm" to go off - in this case Kessen Spirit, and follow the link to profit
8. Stop the program with `CTRL + C`.
9. `CTRL + D` to exit the virtual environment.

## Explanation
What this does is query the Uniqlo backend for a specific product and size, and
if the product's status is `IN_STOCK` then it'll print out the URL, the stock, and you'll be able to order the shirt from the website! (The website might show the size as crossed out but you can just click on it and you'll be able to add to cart). You can add a specific shirt you're trying to look for, and it'll query the backend every minute (this is customizable) for the shirts, and play an mp3 file when the shirt is back in stock.

## Customizations

### Shirts

To add another shirt you want to look for, you need to find it's PID, color ID, and size ID.

Example: https://www.uniqlo.com/us/en/manga-ut-demon-slayer-short-sleeve-graphic-t-shirt-431960.html?dwvar_431960_color=COL00&cgid=ut-graphic-tees-manga-demon-slayer#start=1&cgid=ut-graphic-tees-manga-demon-slayer

The PID is the first value (431960), color ID is the `color=` area (COL00), size_id falls along the pattern of `SMA00*000` where you can replace `*` with your desired size (XXS = 1, XS = 2, SM = 3, M = 4, LG = 5, XL = 6, XXL = 7, 3XL = 8).

Combine the shirt PID with the color ID (in this case `"431960COL00"`) and set it to a variable in `crawler.py` (we'll call this the overall PID).

Then add a tuple of `(PID, size)` to the `SHIRTS` variable in `crawler.py:58`, and next time you run `crawler.py` it should query that endpoint as well.

### Time length
Line 65:
> time.sleep(MIN)

Change the value within `time.sleep` to however often you want to query the endpoint (be careful not to do it too often for rate limiting), the value is in seconds.

### Querying other backends/doing it manually

You can figure out the backend URL for a specific shirt by the following steps:

1. Go to the page for a specific shirt (e.g. https://www.uniqlo.com/us/en/manga-ut-demon-slayer-short-sleeve-graphic-t-shirt-434410.html?dwvar_434410_color=COL00&cgid=ut-graphic-tees-manga-demon-slayer#start=1&cgid=ut-graphic-tees-manga-demon-slayer).
2. Open up the developer tools (assuming you're on Chrome with `CTRL + SHIFT + C`).
3. Go to the Network tab
4. Click the clear button (the 🚫 symbol) to clear all previous traffic.
5. Click on a shirt size (the one you're looking for).
6. Look for the item that starts with `Product-GetAvailability`, right click and Open in New Tab.
7. And voila, you'll be able to see the backend for that specific item, color, and size and the Uniqlo metadata that comes with it. 
