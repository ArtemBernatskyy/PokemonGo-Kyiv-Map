#### Kyiv Pokemon Map Project

### What is ready
- getting Kyiv territory and dividing it in sectors
- Database models are set up completely
- Redis is caching, Celery is working too
- time autodetecting thanks http://momentjs.com/timezone/

### To Do
- celery tasks start scipt to run tasks for active users only
- REST style update map by url path
- Display Pokemon name in templates
- add to Player models status by which we can determine if player can login to PTC ot not (banned or not)
- sometimes Pokemons aren't dissapearing from map and cache