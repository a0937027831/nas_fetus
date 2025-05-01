error_log  /var/log/nginx/error.log warn;
proxy_cache_path /etc/nginx/cache levels=1:2 keys_zone=custom_cache:10m inactive=60m;

server {
    listen ${LISTEN_PORT} ;
    server_name  ${SERVER_NAME} www.${SERVER_NAME};
    
    location /static {
        alias /vol/static;
        expires -1;
    }

    location / {
        include               /etc/nginx/uwsgi_params;
        uwsgi_pass            ${APP_HOST}:${APP_PORT};
        client_max_body_size  10M;
        proxy_cache           custom_cache;
        proxy_cache_valid     any 10m;
        expires               -1;
    }
}