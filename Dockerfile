FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt


COPY ./main.py /code/ 
COPY ./classes.py /code/
COPY ./supabase_functions.py /code/

# Expose the port on which the application will run
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# to change image name for docker hub
#docker tag local-image:tagname new-repo:tagname
#docker push new-repo:tagname