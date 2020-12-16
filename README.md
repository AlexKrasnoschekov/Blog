# Blog
Структура проекта:
1) Папка проекта, папка media и static
2) Файл manage, внутренние папки с телом проекта (blog и myBlog), папка templates(внутри partial(home, single), registration(login) и base.html)
3) Внутри blog (отвечает за структуру собственно блога):
   migrations + init admin views(не спутать с views из myBlog!) apps models tests urls
4) Внутри myBlog (файлы отсюда определяют работу сервера и реализацию манипуляций с адресами/css/localhost):
   init, asgi, settings, urls, views, wsgi
   
