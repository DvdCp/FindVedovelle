# FindVedovelle

FindVedovelle is a web app which shows you a map of Milan where are indicated all Vedovelle located through the city.

What is a Vedovella ? This is a Vedovella !

![alt text](https://github.com/DvdCp/FindVedovelle/blob/main/Vedovella.webp?raw=true)

Grab your bottle and go search for one of them !

## Installation

To run FindVedovelle in local, first download Docker Desktop and Docker Compose clone this repo, go to BeviVedovelle main folder and run:

```bash
docker-compose up --build --remove-orphans --force-recreate
```

This will build a compose with:

- `Nginx` as balance loader
- Main app in `Flask`
- `maptiles_server` to provide maptiles of Milan

Once Docker compose has finished, you should see the website on [http://localhost:8080](http://localhost:8080)

An instance of this project is deployed on EC2 at this link [http://3.79.188.22:8080]

## Improvements

- [ ] Enabling HTTPS
- [ ] Fetching user real position
- [ ] Enter an address to search for
- [ ] Add a nicer and more readable domain
- [ ] Fix pin on vedovelle
