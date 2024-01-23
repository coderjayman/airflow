# airflow
Airflow Docker-Compose

Also see: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

USE AT YOUR OWN RISK. IF YOU DOWNLOAD AND USE THIS YOU ARE RESPONSIBLE.

That being said...

I threw together this UNSECURE DOCKER FILE. NOT FOR PRODUCTION USE. 

There is no SSL or encryption in the database. 

It's for your private playground to learn more about DAG files in Python.

When you start this up you need to access the webserver service container terminal and run:

airflow db init

Not sure why it does not run from the command entered but, hey I just threw this together to play with in my local environment.

Then after it creates all the database tables it will start asking for:

airflow db migrate

When you put a file in the local volume for DAG's just restart the container or run airflow db init again in the webserver container to reload the DAGS.

And where would we be without a Hello World Example?

Well, that's all for now folks... have fun and remember happy coding!





