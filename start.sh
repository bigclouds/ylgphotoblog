docker run --privileged=true  -u root  --network=host -v /srv:/srv:rw -it django-photoblog  /bin/bash
python3 manage.py  runserver 0.0.0.0:9087
# /etc/yum.repos.d/epel.repo
# ffmpeg
# yum install mediainfo ffmpeg ffmpeg-libs -y
