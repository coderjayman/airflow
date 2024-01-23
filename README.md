# airflow
Airflow Docker-Compose

USE AT YOUR OWN RISK. IF YOU DOWNLOAD AND USE THIS YOU ARE RESPONSIBLE.

That being said...

I threw together this UNSECURE DOCKER FILE. <b>NOT FOR PRODUCTION USE<\b>. 

There is no ssl or encryption in the database. 

It's for your own privete playground to learn more about DAG files in python.

When you start this up you need to access the web application terminal and run:

airflow db init

Not sure why it does not run from the command entered but, hey I just threw this together to play with in my local environment.

Then after it creates all the database tables it will start asking for:

airflow db migrate

When you put a file in the local volumn for DAG's just restart the container or run airflow db init again in the airflow container to reload the DAGS.

Well, that's all for now folks... have fun and remember happy coding!



