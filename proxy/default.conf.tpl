error_log  /var/log/nginx/error.log warn;

proxy_cache_path /etc/nginx/cache levels=1:2 keys_zone=custom_cache:10m inactive=60m;
server {
    listen ${LISTEN_PORT} ;

    ssl_certificate             /etc/nginx/ssl/fetus/cert.pem;
    ssl_certificate_key         /etc/nginx/ssl/fetus/privkey.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass               ${APP_HOST}:${APP_PORT};
        include                  /etc/nginx/uwsgi_params;
        client_max_body_size     10M;
        proxy_cache custom_cache;
        proxy_cache_valid any 10m;
    }

    location ~.*\.(jpg|png|jpeg)$ {  
        expires 1d;  
    }

    location ~.*\.(html|js|css)?$ {  
        expires -1;  
    } 
}