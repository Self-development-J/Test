import flask
import server_logger

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello world!"
    
@app.route("/about")
def hello_world():
	return "the about"
	
if __name__ == '__main__':
    host_ = server_logger.get_host()
    port_ = server_logger.get_port()
	app.run(host = host_, port = port_)