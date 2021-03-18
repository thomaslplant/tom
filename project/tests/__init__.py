from application import app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'