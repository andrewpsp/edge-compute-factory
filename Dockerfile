FROM ubuntu:latest As OciOSbase


LABEL vendor=BOdataFactory \
      BusinessObject.Project=BODF-1.0 \
      BusinessOBject.client="BODF" \  
      BusinessOBject.version="0.0.1" \
      BusinessOBj-API.release-date="2023-27-2"


ENV DEV 

RUN echo "hello world" >> base.txt

#documentage / App landing page 

    
