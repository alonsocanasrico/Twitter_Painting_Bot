# Twitter_Painting_Bot

Bot de Twitter que genera una imagen de arte abstracto de manera aleatoria, y la sube en un tweet cada 4 horas. Además, si un usuario de twitter sube un tweet en el que menciona al bot (@ThePaintingBot) junto con uno de estos hashtags: #red / #yellow / #green / #blue / #blackandwhite, el bot generará una imagen de arte abstracto con tonalidades del color elegido en el hashtag, y la publicará mencionando al usuario.
Actualmente el bot no está activo, es decir, no publica de manera automática cada 4 horas ni responde a las menciones, pero cuando se active responderá a todas las menciones que tenga pendientes


El archivo "followers.py" contiene tres métodos que sirven para 
- Seguir a muchos usuarios (y así promocionar la cuenta y conseguir seguidores).
- Dejar de seguir a todas las cuentas (tras conseguir seguidores no es necesario seguir a todas las cuentas que se suiguieron para promocionar).
- Eliminar "me gusta" de todos aquellos tweets a los que se les haya dado "me gusta" (por si se da "me gusta" a publicaciones con tal de promocionar la cuenta, y después no interesa que aparezcan entre los tweets favoritos).
