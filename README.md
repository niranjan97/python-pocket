# python-pocket
Uses python-requests to connect with GetPocket (http://www.getpocket.com) to retrieve information. 
Still in build, kind of broken considering the fact that I didn't plan ahead and peek at the Pocket API; only realizing too late that retrieving actual articles off of Pocket is next to impossible.

So far, have built the authentication side of the application. Need to build the user-side, with adding items, removing items and (hopefully) extracting items to a .txt for offline use. 
Request functions all work as they should. You don't have to use my API consumer_key. Check out https://getpocket.com/developer/docs/authentication for more info. 

 
EDIT: Welp, nevermind. Turns out Pocket doesn't support article extraction (https://getpocket.com/developer/docs/v3/article-view). I'll leave the authentication stuff here if anyone wants to use it though, and might add basic add/remove functionality to round out the application. You could always use Diffbot as the attached webpage suggests however.

I know I won't.
