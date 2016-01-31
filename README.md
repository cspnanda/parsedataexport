Insert a Data Dump from Parse to MongoLab. Go to your Parse dashboard and export data. When it is complete, you get an email

  1. First install Python and pymongo module (sudo pip install pymongo)

  2. Get the attached insert.py and run it as ./insert.py CLASSNAME.son 
     (CLASSNAME is your custom class from Data Dump from Parse)

This will output a view which you can attach to MongoLab Table view and get a display like Parse Table View.

    $ ./insert.py BUCKET.json 
       Your Table View
     {
	"placeName":"placeName",
	"objectId":"objectId",
	"placeId":"placeId",
	"location":"location",
	"updatedAt":"updatedAt",
	"createdAt":"createdAt"
     }

Insert Into Mongo: [######              ] 32%
