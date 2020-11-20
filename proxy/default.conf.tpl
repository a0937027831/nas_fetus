error_log  /var/log/nginx/error.log warn;

server {
    listen ${LISTEN_PORT} ;

    ssl_certificate             /etc/ssl/fetus/cert.pem;
    ssl_certificate_key         /etc/ssl/fetus/privkey.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass               ${APP_HOST}:${APP_PORT};
        include                  /etc/nginx/uwsgi_params;
        client_max_body_size     10M;
    }
}