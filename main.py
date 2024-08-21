from flask import Flask, jsonify, json, request, Response, send_file
app = Flask(__name__)

import system.payments
import system.security



import logging
terminal_output  =  False


if terminal_output:
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)


#Rotas de paginas
@app.route("/") #Landpage ou pagina principal
def home():
    return send_file('./archives/templates/index.html')


#Rotas Genericas
@app.route("/script/<code>")
def code(code):
    return send_file(f'./archives/scripts/{code}.js')

@app.route("/style/<style>")
def style(style):
    return send_file(f'./archives/styles/{style}.css')

@app.route("/image/<path>/<image>")
def image(path,image):
    return send_file(f'./archives/images/{path}/{image}.png')

@app.route("/font/<font>")
def font(font):
    return send_file(f'./archives/fonts/{font}')

@app.route("/qr/<id>")
def qrcode(id):
    return send_file(f'./archives/images/qrcodes/{id}.png')


#Rotas POST
@app.route("/login/submit", methods=['POST'])
def login_submit():
    args = request.json
    ip = request.remote_addr
    device = request.user_agent

    print(args)
    if 'username' in args.keys() and 'password' in args.keys():
        system.security.login_user(ip, device, args['username'], args['password'])
        return {'result':True}
    return {'result':False}

@app.route("/get_qr", methods=['POST'])
def get_qr():
    args = request.json
    ip = request.remote_addr
    device = request.user_agent

    print(args)
    if 'value' in args.keys():
        qr = system.payments.get_qrcode(args['value'])
        return qr
    return {'result':False}



if __name__ == "__main__":
    app.run(debug=True, port=5050)
else:
    print('System not started')
    