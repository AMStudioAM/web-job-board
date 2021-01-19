Tutor For Course: 
static files: [frontend] images(baaner, header background), css, javascript 
media files: [upload] images(profile photo)


Form in django:
- enctype 'multipart/form-data'

view.py with form in django:
- request.method('POST') # when you don't want to show the url 
- request.method('GET') # when you want to show the url 
- FormVar = FormApplication(request.POST, request.FILES)
