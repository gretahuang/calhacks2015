from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
import flask.ext.whooshalchemy as whooshalchemy
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User, Landlord, Review, LLProperty
from oauth import OAuthSignIn

whooshalchemy.whoosh_index(app, Student)
whooshalchemy.whoosh_index(app, Project)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    user = g.user
    return render_template('index.html',
                           title='Index')

@app.route('/search')
def search():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect(url_for('search', query=search_form.query.data))

@app.route('/search/<query>')
def search_results(query):   
    search_form = SearchForm()
    if search_form.validate_on_submit():
        return redirect(url_for('search', query=search_form.query.data))

    landlord_results = Landlord.query.whoosh_search(query, MAX_SEARCH_RESULTS).\
                       filter_by(confirmed=True).all()

    best_landlords = Landlord.query.order_by(Landlord.avg_rating)[:5]
    worst_landlord = Landlord.query.order_by(Landlord.avg_rating.desc())[:5]

    return render_template('searchpage.html',
                            title='Search',
                            landlord_results=landlord_results,
                            best_landlords=best_landlords,
                            worst_landlords=worst_landlords,
                            search_form = SearchForm())

@app.route('/profile/<id>')
def landlord_profile(id):
    return render_template('landlord_profile.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

# errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
