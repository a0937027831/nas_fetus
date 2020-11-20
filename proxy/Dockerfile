FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="a0937027831@gmail.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params

ENV LISTEN_PORT=8000
ENV APP_HOST=fetus
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static
RUN mkdir -p /etc/nginx/ssl/fetus
COPY ./archive/cert.pem /etc/nginx/ssl/fetus/cert.pem
COPY ./archive/privkey.pem /etc/nginx/ssl/fetus/privkey.pem
RUN chmod 755 /vol/static
RUN touch /etc/nginx/conf.d/default.conf
RUN chown nginx:nginx /etc/nginx/conf.d/default.conf /etc/nginx/ssl/fetus/cert.pem /etc/nginx/ssl/fetus/privkey.pem



COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER nginx

CMD ["/entrypoint.sh"]