from app import app
from ..emails import contact_submit

from flask import render_template, abort


@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/gallery/<gallery_type>')
def gallery(gallery_type):
  """
  Returns the corresponding template based on the gallery_type (ex: Wedding, Family, ect).

  Note: This might be revamped to just query the database.
  """
  if gallery_type == 'wedding':
    return render_template('gallery/wedding.html')
  elif gallery_type == 'themed':
    return render_template('gallery/themed_sessions.html')
  elif gallery_type == 'headshots':
    return render_template('gallery/headshots.html')
  elif gallery_type == 'maternity':
    return render_template('gallery/maternity.html')
  elif gallery_type == 'birth':
    return render_template('gallery/birth_photos.html')
  elif gallery_type == 'family':
    return render_template('gallery/family.html')
  else:
    abort(404)


@app.route('/contact')
def contact():
  contact_submit('Mark', 'Laskey', 'laskey.mark@hotmail.com', '2018-07-04')

  return render_template('contact.html')

