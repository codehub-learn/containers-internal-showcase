#!/bin/bash
for x in {1..100}; do 
    name="user-$(( $RANDOM % 1000 ))"
    id="$(openssl rand -hex 2)" 
    ext="d$(openssl rand -hex 1)"
    surname="surname-$id"
    home_page="http://www.home$id.$ext"
    friends="$(( $RANDOM % 100 ))"
    echo INSERT "INTO users (id,name,surname,friends,home_page) VALUES (NULL,\"$name\",\"$surname\",\"$friends\",\"$home_page\");"; 
done
