from app import app
from app.forms import ContactForm
from ..emails import contact_submit

from flask import render_template, abort, flash, url_for, redirect


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
    return abort(404)


@app.route('/investments/<inv_type>')
def investments(inv_type):
  if inv_type == 'wedding':
    return render_template('investments/wedding.html')  
  elif inv_type == 'themed':
    return render_template('investments/themed_sessions.html')
  elif inv_type == 'maternity':
    return render_template('investments/maternity.html')
  elif inv_type == 'headshots':
    return render_template('investments/headshots.html')
  elif inv_type == 'family':
    return render_template('investments/family.html')
  elif inv_type == 'birth':
    return render_template('investments/birth_photos.html')
  elif inv_type == 'boudoir':
    return render_template('investments/boudoir.html')
  return abort(404)

  
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if form.validate_on_submit():
    contact_submit(form.data['first_name'], form.data['last_name'], form.data['email'], form.data['date'])

    url = url_for('contact')
    flash('Thank you for sending an email.  We will get back to you soon.')
    return redirect(url)

  return render_template('contact.html', form=form)

