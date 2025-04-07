from flask import Flask, request, jsonify
from extensions import db, migrate, init_app
from models import Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    
    episode_data = episode.to_dict()
    episode_data['appearances'] = [
        {
            'episode_id': appearance.episode_id,
            'guest': appearance.guest.to_dict(),
            'guest_id': appearance.guest_id,
            'id': appearance.id,
            'rating': appearance.rating
        }
        for appearance in episode.appearances
    ]
    return jsonify(episode_data)

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id,
            'episode': appearance.episode.to_dict(),
            'guest': appearance.guest.to_dict()
        }), 201
        
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        return jsonify({'errors': ['Validation errors']}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
