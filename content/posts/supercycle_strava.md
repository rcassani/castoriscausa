Title: SuperCycle data to Strava
Date: 2023-10-07 19:00
Modified: 2023-10-22 17:00
Tags: bike, SQLite, Python, REST
Author: Raymundo Cassani
Slug: supercycle_strava
Thumbnail: supercycle2gpx2strava.png

**Updated**: Now exporting rides from the [Zeopoxa cycling](https://www.zeopoxa.com/cycling.html) app to GPX files is also supported.

Recently I moved to the [Strava app](https://www.strava.com) to register the my biking activity. However, I had plenty of data recorded with the [SuperCycle app](http://www.osborntech.com/). So, I code my way to migrate the data. First, each ride recorded with SuperCycle was stored as [GPX, or GPS Exchange Format files](https://en.wikipedia.org/wiki/GPS_Exchange_Format), after converting all the rides, the GPX files were uploaded to Strava using their API. The codes for this project can be found in:

[https://github.com/rcassani/supercycle_strava](https://github.com/rcassani/supercycle_strava)

## SuperCycle data to GPX
SuperCycle data is stored in a [SQLite](https://www.sqlite.org/index.html) database. A copy of the database can be generated with the **Create backup** option in the the app. Among all the data in the database, we are interested in three tables:

* **bike** : Information for bikes
* **ride** : Summary information for rides
* **ride_detail**:  Localization resolved at one-second for each ride

Reading the database tables and writing the GPX files is done with [`supercyle2gpx.py`](https://github.com/rcassani/supercycle_strava/blob/main/supercyle2gpx.py)

## Zeopoxa data to GPX
Zeopoxa data is also stored in a SQLite database, but its schema table is different. A copy of the database can be generated with the **Backup** option in the the app. Among all the data in the database, we are interested in only tables:

* **main_table** : Information for rides with localization resolved at one-second
* **bicycle_table** : Information for bikes

Reading the database tables and writing the GPX files is done with [`zeopoxa2gpx.py`](https://github.com/rcassani/supercycle_strava/blob/main/zeopoxa2gpx.py)

## Upload GPX files to Strava
Strava allows to manually upload GPX files using [this page](https://www.strava.com/upload/select).

But it is not practical if several files need to be uploaded, as it is the case here. As such, the upload of files can be done through their [API](https://developers.strava.com/docs/reference/).

Before using it, it is necessary to follow these [steps to create your API application](https://developers.strava.com/docs/getting-started/). This process will give your `client_id` and `client_secret` that are needed to use the API, and the code below to upload the GPX files.

Connecting to Strava, getting the permission and uploading the GPX files happens in [`gpx2strava.py`](https://github.com/rcassani/supercycle_strava/blob/main/gpx2strava.py)

## All data in one place
With all the ride data in one place, it is possible to do some nice maps.
More over, [data from Strava can be exported in bulk](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export).  

<center>
[<img src="/images/some_activities.png" style="width: 80%;">](/images/some_activities.png)<br>
**Bike activity heatmap**
</center>

## References
* [https://developers.strava.com/docs/getting-started/](https://developers.strava.com/docs/getting-started/)
* [https://developers.strava.com/docs/authentication/](https://developers.strava.com/docs/authentication/)
* [https://developers.strava.com/docs/uploads/](https://developers.strava.com/docs/uploads/)
* [https://yizeng.me/2017/01/11/get-a-strava-api-access-token-with-write-permission/](https://yizeng.me/2017/01/11/get-a-strava-api-access-token-with-write-permission/)
