from app import app
from flask import render_template

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/topfive')
def top_five():
    fav_artists = [{'name':'Sydney Doemel', 'img':'https://www.seraphicfire.org/wp-content/uploads/2022/01/Sydney-Doemel.jpeg','genre':'Electroacoustic Experimental', 'link': 'https://soundcloud.com/sydney-doemel'},
{'name':'Sahada Buckley', 'img':'https://static.wixstatic.com/media/5bff65_1f036bd9c7d7466193e3f14276b2fddb~mv2.jpeg/v1/fill/w_560,h_852,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/IMG_4575.jpeg','genre':'Experimental Improvisation', 'link': 'https://www.youtube.com/channel/UC6iKaHCODGBgPKEOgywgqXw'},
{'name':'Daniel Phipps', 'img':'https://i.ibb.co/k15kCWw/dan-headshot-4.jpg','genre':'Contemporary Classical Saxophone', 'link': 'https://soundcloud.com/kevindaymusic/unquiet-waters-i-fast-turbulent'},
{'name':'Annie Leeth', 'img':'https://i.ibb.co/qYRVBdk/annie-pic.jpg','genre':'Deep New Americana', 'link': 'https://annieleeth.bandcamp.com/'},
{'name':'Jason Bronson', 'img':'https://i.ibb.co/S0KSrsf/IMG-689-E847-B3024-1.jpg','genre':'Singing Saw, Sunshine Pop', 'link': 'https://sibyllinelover.bandcamp.com/track/winter-isolation'}]
    return render_template('top_five.html', fav_artists=fav_artists)

