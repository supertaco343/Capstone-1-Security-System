# Project Timeline

### Week 1 (October 7th - 13th)
* Found a dataset that will be useful for identifying one of our desired events (deliveries). The [box dataset](https://universe.roboflow.com/craig-test-workspace/doorbell-camera-alert) can be used to train an ai model that can detect a box in a live recording. The detection will then send a notification to the user, alerting them of the delivery.
* Going to use the yolov11 model from ultralytics and train it on the box dataset.

### Week 2 (October 14th - 20th)
* Decided to use the python application framework Flask as it is fairly simple framework.
* Decided to use SQLite for the database since the data to be stored can be local and isn't too complex
* Created a starter schema for the database represented by the schema.sql file.
* Built a couple API routes to allow for adding cameras to the database, querying the cameras in the database, and viewing the home page.

### Week 3 (October 21st - 27th)