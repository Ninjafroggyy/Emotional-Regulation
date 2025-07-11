# backend/http api documentation


### GET `/random/<zoneString>`

 * description: returns a random activity for the given zone colour
 * inputs: zone colour found in url [str]
 * outputs: activity [json format string] 
 * change: if we had more time we would change this to return an activity ID and an activity name in the json response on /random)

### GET `/activitylink/`

 * description: takes in a random activity and returns an http link to the online resource
 * inputs: activity ID [int] 
 * outputs: http link to resource for given activity [json link]

